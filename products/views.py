from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None) # Objeto do form do tipo ProductForm é criado, ou seja, deve conter todos os campos obrigatórios
    if request.method == "POST" and form.is_valid(): # Se o método for POST e o formulário enviado for válido, o Django salva no BD
        form.save()
        form = ProductForm() # Depois de salvar já cria um novo formulário

    context = {
        'form': form
    }
    return render(request, "products/products_create.html", context)

def product_create_view2(request):
 '''if request.method == "POST":
        name = request.POST.get('title') 
        print(name) # Printa no servidor
        context = {}
        return render(request, "products/products_create2.html", context)'''

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # a manutenção/edição de um contexto com todos os campos do model não é muito eficiente
    '''context = {
        'name': obj.name,
        'price': obj.price
    }'''

    context = {
        'object': obj
    }
    return render(request, "products/products_detail.html", context)