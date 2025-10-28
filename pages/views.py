from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return render(request, "home.html", {}) # request é um objeto do Django que representa tudo que veio do navegador ou cliente

def about_view(request):
    about_context = { # dicionário que passa variáveis para o template
<<<<<<< HEAD
        "my_text": "hey! This is about us",
        "my_number": 123,
        "my_list": [123, 456, 789],
        "my_html": "<h3>Esse texto possui tags html que não são renderizadas por conta do safe</h3>"
=======
        "about_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 456, 789],
>>>>>>> 7c0c3b90d21e6d8389c65c83029ecb6a6828c71f
    }
    return render(request, "about.html", about_context) # request é um objeto do Django que representa tudo que veio do navegador ou cliente