from django.db import models
from django.contrib import admin
class Flor(models.Model):

    nombre  =   models.CharField(max_length=30)
    caracteristica  =   models.CharField(max_length=30)
    color  =   models.CharField(max_length=30)
    precio  =    models.IntegerField()
    def __str__(self):
        return self.nombre

class Ramo(models.Model):
    nombre    = models.CharField(max_length=60)
    total     = models.IntegerField()
    flores   = models.ManyToManyField(Flor, through='Ramito')
    def __str__(self):
        return self.nombre
class Ramito (models.Model):
    flor = models.ForeignKey(Flor, on_delete=models.CASCADE)
    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE)

class RamitoInLine(admin.TabularInline):
    model = Ramito
    extra = 1

class FlorAdmin(admin.ModelAdmin):
    inlines = (RamitoInLine,)

class RamoAdmin(admin.ModelAdmin):
    inlines = (RamitoInLine,)
