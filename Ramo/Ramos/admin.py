from django.contrib import admin
from Ramos.models import Flor, FlorAdmin, Ramo, RamoAdmin
admin.site.register(Flor, FlorAdmin)
admin.site.register(Ramo, RamoAdmin)

# Register your models here.
