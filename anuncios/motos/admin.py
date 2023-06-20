from django.contrib import admin
from .models import Marca,Moto,Tag,Opcional,Combustivel

# Register your models here.
admin.site.register(Marca)
admin.site.register(Moto)
admin.site.register(Tag)
admin.site.register(Opcional)
admin.site.register(Combustivel)
