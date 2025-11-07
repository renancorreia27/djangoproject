"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, about_view # Importa views específicas do app pages
from products.views import product_all_view, product_create_view, dynamic_lookup_view, product_detail_view

urlpatterns = [
    # Os caminhos name/ acessam suas funções que devolvem páginas web
    path('about/', about_view, name='about'),
    path('', home_view, name='home'),
    path('product/create/', product_create_view, name='create'),
    path('product/', product_all_view, name='list'),
    path('product/edit/<int:product_id>', dynamic_lookup_view, name='view'),
    path("product/view/<int:product_id>/", product_detail_view, name="product-detail"),
    path('admin/', admin.site.urls),
]