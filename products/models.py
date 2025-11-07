from django.db import models

# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length=120)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    description = models.TextField(blank=True, null=True)
    sale        = models.BooleanField(null=True) # Campo obrigatório pois não pode ser nulo

    def edit_object(self):
        return f"/product/edit/{self.id}"
    
    def view_object(self):
        return f"/product/view/{self.id}"