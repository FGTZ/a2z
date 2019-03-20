
from django.db import models

# Create your models here.
class User(models.Model):

   # gender = (
   #     ('male'),
   #     ('female'),
   # )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    userEmail = models.EmailField(verbose_name='Customer_Email', max_length=128, unique=True)
    billAddr = models.CharField(verbose_name='Billing_Address', null=True, max_length=150)
    shipAddr = models.CharField(verbose_name='Shipping_Address', null=True, max_length=150)
    contact = models.CharField(null=True, max_length=150)
   # sex = models.CharField(max_length=32, choices=gender, default='male')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'users'
        verbose_name_plural = 'users'

class Computer(models.Model):
    computerId= models.IntegerField(primary_key=True)
    computerName = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    processor = models.CharField(null=True, max_length=300)
    memory = models.CharField(null=True, max_length=300)
    hardDrive = models.CharField(null=True, max_length=300)
    display = models.CharField(null=True, max_length=300)
    operating = models.CharField(null=True, verbose_name='Operating_System', max_length=300)
    price = models.IntegerField()
    stock = models.IntegerField()
    #picture = models.ImageField(upload_to='product', verbose_name='Product_Image', null=True)#

class Accessories(models.Model):
    accessoriesId= models.IntegerField(primary_key=True)
    accessoriesName = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    stock = models.IntegerField()
    #picture = models.ImageField(upload_to='product', verbose_name='Accessories_Image')


class Categories(models.Model):
    categoriesId = models.IntegerField(primary_key=True)
    categoriesName = models.CharField(max_length=300)

class Customize(models.Model):
    customizeId= models.IntegerField(primary_key=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    customizeName = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    stock = models.IntegerField()
    #picture = models.ImageField(upload_to='product', verbose_name='Customize_Image')

class Order(models.Model):
    orderNo = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('User',on_delete=models.CASCADE)
    billAddr = models.CharField(verbose_name='Billing_Address', null=True, max_length=150)
    shipAddr = models.CharField(verbose_name='Shipping_Address', null=True, max_length=150)
    amount = models.IntegerField()
    orderTime = models.DateTimeField(auto_now_add=True)

class OrderDetail(models.Model): #Please help to finish this table.
    orderNo = models.ForeignKey('Order',on_delete=models.CASCADE)
    item = models.ForeignKey('Computer', on_delete=models.CASCADE)#这里应该是要查三个表格的
    quantity = models.IntegerField()
    price = models.IntegerField()
