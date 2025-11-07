from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length=120)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    description = models.TextField(blank=True, null=True)
    sale        = models.BooleanField(null=True) # Campo obrigatório pois não pode ser nulo


    # Gera automaticamente a URL de edição usando o nome da rota definido em urls.py. Isso evita erros caso o caminho mude, pois o Django resolve a URL com base no nome ("edit").
    def edit_object(self):
        return reverse("products:edit", kwargs={"product_id": self.id})
        # Exemplo alternativo (menos seguro): return f"/product/edit/{self.id}" - Esse formato é fixo e precisaria ser alterado manualmente se a rota fosse modificada.
    
    def view_object(self):
        return reverse("products:view", kwargs={"product_id": self.id})