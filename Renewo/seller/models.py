from django.db import models

# Create your models here.

# Seller database
class homeseller(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone= models.IntegerField(unique=True)
    address = models.CharField(max_length=255)
    pincode= models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    seller_id=models.CharField(max_length=20, null=True , blank=True)


    def __str__(self) -> str:
        return self.first_name