from django.contrib import admin
from .models import Guitar, Maintenance, Accessory
# Register your models here.

admin.site.register(Guitar)
admin.site.register(Maintenance)
admin.site.register(Accessory)