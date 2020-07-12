from django.contrib import admin
from .models import Workings, Servicing

# Register your models here.
admin.site.register(Servicing)
admin.site.register(Workings)