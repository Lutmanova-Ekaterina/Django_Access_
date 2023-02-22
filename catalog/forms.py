from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        allowed_name = cleaned_data.get('product_name')
        allowed_title = cleaned_data.get('title')
        if allowed_name and allowed_title:
            if ('казино' or 'криптовалюта' or 'крипта' or 'биржа' or 'дешево' or 'бесплатно' or 'обман' or 'полиция' or 'радар') in (allowed_name and allowed_title):
                raise forms.ValidationError("Название и описание не должны содержать запрещенных слов")
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
