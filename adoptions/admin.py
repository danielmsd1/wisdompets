from django.contrib import admin

from .models import Pet

@admin.register(Pet)

class PetAdmin(admin.ModelAdmin):
    list_diplay = ['name','species','breed','age','sex']
    