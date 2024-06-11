from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    items_supplied = models.ManyToManyField(Item, related_name='suppliers', blank=True)

    def __str__(self):
        return self.name
