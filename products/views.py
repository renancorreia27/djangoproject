from django.shortcuts import render
<<<<<<< HEAD
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
    return render(request, "product/detail.html", context)
=======

# Create your views here.
>>>>>>> 7c0c3b90d21e6d8389c65c83029ecb6a6828c71f
