from django.urls import path
from products.views import product_all_view, product_create_view, dynamic_lookup_view, product_detail_view

app_name = 'products' # Define o namespace do app para evitar conflitos de rotas
urlpatterns = [
    path('', product_all_view, name='list'),
    path('create/', product_create_view, name='create'),
    path('edit/<int:product_id>/', dynamic_lookup_view, name='edit'),
    path("view/<int:product_id>/", product_detail_view, name='view'),
]