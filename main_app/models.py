from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    details = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("accessory_detail", kwargs={"pk": self.id})
    

class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    guitar_type = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return f'{self.brand} {self.model}'

    def get_absolute_url(self):
        return reverse("detail", kwargs={"guitar_id": self.id})
    
    def future_maintenance_scheduled(self):
        count = 0
        for maintenance in self.maintenance_set.all():
            if maintenance.date > date.today():
                count += 1
        return count > 0
    
    def get_current_date(self):
        return date.today()

class Maintenance(models.Model):
    date = models.DateField('maintenance date')
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__ (self):
        return f'Maintenance Schedule on {self.date}'

    class Meta:
        ordering = ['date']