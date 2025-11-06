from django.http import Http404
from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_create_view(request):
    initial_data = {
        "name": "Name a new product"
    }

    form = ProductForm(request.POST or None, initial = initial_data) # Objeto do form do tipo ProductForm é criado, ou seja, deve conter todos os campos obrigatórios
    if request.method == "POST" and form.is_valid(): # Se o método for POST e o formulário enviado for válido, o Django salva no BD
        form.save()
        form = ProductForm() # Depois de salvar já cria um novo formulário

    context = {
        'form': form
    }
    return render(request, "products/products_create.html", context)

def dynamic_lookup_view(request, product_id):
    try:
        obj = Product.objects.get(id = product_id)
    except Product.DoesNotExist:
        raise Http404

    form = ProductForm(request.POST or None,
                        instance = obj) # instance modela um objeto já existente do banco
    if request.method == "POST" and form.is_valid(): # Se o método for POST e o formulário enviado for válido, o Django salva no BD
        form.save()
        form = ProductForm() # Depois de salvar já cria um novo formulário

    context = {
        'form': form
    }
    return render(request, "products/products_view.html", context)

def product_all_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "products/products_all.html", context)

# A manutenção/edição de um contexto com todos os campos do model não é muito eficiente
    '''context = {
        'name': obj.name,
        'price': obj.price,
    }'''