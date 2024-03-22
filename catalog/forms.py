from django.forms import ModelForm, forms

from catalog.models import Product, Version


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name').lower()
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'В названии продукта не должно быть слова {word}')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description').lower()
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'В описании продукта не должно быть слова {word}')
        return cleaned_data


class VersionForm(ModelForm):

    class Meta:
        model = Version
        fields = ('__all__',)

