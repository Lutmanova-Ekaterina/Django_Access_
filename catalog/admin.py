from django.contrib import admin

from catalog.models import Product, Category, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category')
    search_fields = ('name', 'title')
    list_filter = ('category', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('head', 'views_number', 'slug', 'content', 'date_create', 'publication')
    prepopulated_fields = {"slug": ("content",)}
