from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    collection_date = models.DateField()
    current_date = models.DateField(auto_now_add=True)
    collected = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name



