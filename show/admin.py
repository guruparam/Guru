from django.contrib import admin
from show.models import Brand, Phonemodel

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = 'name', 'image'

class PhonemodelAdmin(admin.ModelAdmin):
    list_display = 'brand', 'name', 'released_year', 'price', 'image'

admin.site.register(Brand,BrandAdmin)
admin.site.register(Phonemodel,PhonemodelAdmin)