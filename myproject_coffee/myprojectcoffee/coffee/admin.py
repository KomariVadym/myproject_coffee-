from django.contrib import admin
from .models import Coffee

class CoffeAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity','image')


admin.site.register(Coffee,CoffeAdmin)
