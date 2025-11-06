from django import forms
from  .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product # este formulário representa o modelo Product
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

    # o Django automaticamente o chamará quando o formulário for validado
    def clean_name(self, *args, **kwargs): # clean_<campo>()
        name = self.cleaned_data.get("name") # cleaned_data → contém os valores já processados e válidos. get("name") → pega o valor do campo name.
        if "CFE" in name:
            raise forms.ValidationError("Isso não é um nome válido!")
        return name