from django.contrib import admin
from django.db.models import F 
from tienda.models import Categoria, Producto, Cliente

admin.site.register(Categoria)

admin.site.register(Cliente)

def increase_price(modeladmin, request, queryset):
    queryset.update(precio=F('precio') + 1)
increase_price.short_description = "Aumentar precio"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'pub_date')
    list_filter = ('nombre', 'precio', 'stock', 'pub_date', 'categoria')
    actions = [increase_price]
    actions_on_top = True
    actions_on_bottom = True

admin.site.register(Producto,ProductAdmin)