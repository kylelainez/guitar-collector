from django.db import models
from django.urls import reverse

# Create your models here.

class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    guitar_type = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.brand} {self.model}'

    def get_absolute_url(self):
        return reverse("home", kwargs={"guitar_id": self.id})
    