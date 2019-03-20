from django.contrib import admin
from . import models
# Register your models here.
from .models import User, Computer, Accessories, Categories, Customize, Order, OrderDetail


class UserAdmin(admin.ModelAdmin):
    list_display = ('name','password','userEmail','billAddr','shipAddr','contact','create_time')
admin.site.register(User, UserAdmin)

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('computerId','computerName','description','processor','memory','hardDrive','display','operating','price','stock')#'picture')
admin.site.register(Computer, ComputerAdmin)

class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('accessoriesId','accessoriesName','description','price','stock')#'picture')
admin.site.register(Accessories, AccessoriesAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('categoriesId','categoriesName')
admin.site.register(Categories, CategoriesAdmin)

class CustomizeAdmin(admin.ModelAdmin):
    list_display = ('customizeId', 'category','customizeName','description','price','stock')#'picture')
admin.site.register(Customize, CustomizeAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderNo','customer','billAddr','shipAddr','amount','orderTime')
admin.site.register(Order, OrderAdmin)

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('orderNo', 'item','quantity','price')
admin.site.register(OrderDetail, OrderDetailAdmin)
