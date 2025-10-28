from django.shortcuts import render
from .models import Product

# Create your views here.
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