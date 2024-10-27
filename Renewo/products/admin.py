from django.contrib import admin
from products.models import order,Customer, oderitem, ShippingAddress, Product , Cart,CartItem

# Register your models here.
admin.site.register(order)
admin.site.register(oderitem)
admin.site.register(ShippingAddress)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Cart)