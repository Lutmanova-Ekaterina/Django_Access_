from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product, Blog, Version
from catalog.forms import ProductForm, VersionForm
from catalog.service import cache_category
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


def pictures(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/pictures.html', context)


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = cache_category(self)
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    raise_exception = True
    permission_denied_message = "Access is restricted to authenticated users"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    raise_exception = True
    permission_denied_message = "Access is restricted to authenticated users"

    def get_queryset(self):
        return Product.objects.filter(user_create=self.request.user)

    def test_func(self):
        product = self.get_object()
        return product.user_create == self.request.user or self.request.user.has_perms(
            perm_list=['set_sign_of publication', 'change_description_product', 'change_category_product'])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')
    raise_exception = True
    permission_denied_message = "Access is restricted to authenticated users"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    raise_exception = True
    permission_denied_message = "Access is restricted to authenticated users"


class VersionView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    template_name = 'catalog/product_version.html'
    raise_exception = True
    permission_denied_message = "Access is restricted to authenticated users"

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        print(self.request.method)
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication=Blog.STATUS_ACTIVE)

        return queryset


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('catalog:blog')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('catalog:blog')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')


class BlogDetailView(DetailView):
    model = Blog

    def get(self, *args, **kwargs):
        blog_item = get_object_or_404(Blog)
        blog_item.views_number += 1
        blog_item.save()
        return super().get(self, *args, **kwargs)


def change_status(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.publication == Blog.STATUS_ACTIVE:
        blog_item.publication = Blog.STATUS_INACTIVE
    else:
        blog_item.publication = Blog.STATUS_ACTIVE
    blog_item.save()

    return redirect(reverse('catalog:blog'))
