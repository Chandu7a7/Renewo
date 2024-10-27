from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class order(models.Model):
    customer_name = models.ForeignKey(User, on_delete=models.SET_NULL , null=True , blank=True)
    date_order = models.DateField()
    complete_order = models.DateField()
    transaction_id = models.CharField(max_length=255)
    def __str__(self):
        return str(self.customer_name)  # Convert customer_name to a string

    @property
    def name(self):
        return f"Order {self.id}"
    

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_decp = models.CharField(max_length=255)
    product_imp = models.ImageField(null=True , blank=True)

    def __str__(self) -> str:
        return self.product_name
    
    @property
    def imageURL(self):
        try:
            url=self.product_imp.url
        except:
            url=''
        return url
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)  
    
class oderitem(models.Model):
    product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True , blank=True)
    order = models.ForeignKey(order , on_delete=models.SET_NULL , null=True , blank=True)
    quantity = models.IntegerField(default=0 , null=True , blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):

    customer_name = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True)
    order = models.ForeignKey(order , on_delete=models.SET_NULL , null=True , blank=True)
    address = models.CharField(max_length=255 )
    city = models.CharField(max_length=255 )
    pincode = models.CharField(max_length=255 )
    state = models.CharField(max_length=255 )
    date_added =models.DateTimeField(auto_now_add=True)


    def __str__(self):
      if self.customer_name:
        return f"Order #{self.id} for {self.customer_name.username}"
      else:
        return f"Order #{self.id}"
 
class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, null=True , blank=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255 , null=True)
    cart = models.OneToOneField(Cart, on_delete=models.SET_NULL, null=True, blank=True)