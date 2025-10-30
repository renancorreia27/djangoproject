from django import forms
from  .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={ # attrs = atributos html
                'class': 'form-control', # como o css vai reconhecer o campo 'name'
                'placeholder': 'Nome do produto' # texto que aparece no campo
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Preço em reais'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição do produto',
                'rows': 3
            }),
        }