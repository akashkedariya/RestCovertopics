from django.contrib import admin
from .models import CustomUser, Product, Customers


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ( 'id','f_name', 'l_name', 'email', 'password' )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'id','product_name', 'price', 'quantity' ]


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = [ 'customer_id', 'first_name', 'phone', 'price', 'street', 'city', 'product' ]






