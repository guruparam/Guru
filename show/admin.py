from django.contrib import admin
from show.models import Brand, Phonemodel, Transaction

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = 'name', 'image'

class PhonemodelAdmin(admin.ModelAdmin):
    list_display = 'brand', 'name', 'released_year', 'price', 'image'

class TransactionAdmin(admin.ModelAdmin):
    list_display = 'user', 'model', 'transaction_type', 'amount'

admin.site.register(Brand,BrandAdmin)
admin.site.register(Phonemodel,PhonemodelAdmin)
admin.site.register(Transaction,TransactionAdmin)