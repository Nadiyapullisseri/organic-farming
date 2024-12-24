from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerprofilePic/',null=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    
class Farmer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerprofilePic/',null=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    
class Product(models.Model):
    product_name=models.CharField(max_length=40)
    product_image=models.ImageField(upload_to='product_image/',null=True)
    product_price=models.IntegerField()
    product_discription=models.CharField(max_length=40)
    
class Feedback(models.Model):
    feedback_name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=40)
    date=models.DateField()
    
class Query(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    query=models.CharField(max_length=40)
    replay=models.CharField(max_length=40,default='nothing')
    query_date=models.DateField(auto_now=True)
    
class Notice(models.Model):
    message=models.CharField(max_length=40)
    message_date=models.DateField(auto_now=True)
    
class Payment(models.Model):
    card_number=models.CharField(max_length=40)
    mobile_number=models.IntegerField()
    expiry_date=models.DateField()
    cvv=models.IntegerField()
    account_holder_name=models.CharField(max_length=40)
    amount_to_pay=models.IntegerField(default='0')
    

    