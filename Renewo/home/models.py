from django.db import models 
# from home.models import order , Product , oderitem 

from django.contrib.auth.models import User 





 


#company dbase
class company(models.Model):
    companyname = models.CharField(max_length=255)
    companylast=models.CharField(max_length=255,default='company')
    companyphone= models.CharField(max_length=12,unique=True )
    companyaddress = models.CharField(max_length=255)
    pincode= models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    company_id=models.CharField(max_length=20,null=True ,blank=True )

    def __str__(self) -> str:
        return self.companyname



