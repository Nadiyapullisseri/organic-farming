from dataclasses import field, fields
from django import forms
from django.contrib.auth.models import User
from .import models
from .models import Farmer, Notice, Product, Query, User,Customer,Feedback,Payment






class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','password','username']
        widgets={
            'password': forms.PasswordInput()
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['address','mobile','profile_pic']
        
        


class FarmerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','password','username']
        widgets={
            'password':forms.PasswordInput()
        }
class FarmerForm(forms.ModelForm):
    class Meta:
        model=Farmer
        fields=['address','mobile','profile_pic']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['product_name','product_image','product_price','product_discription']
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['feedback_name','feedback','date']

class QueryForm(forms.ModelForm):
    class Meta:
        model=Query
        fields=['query']
        
class NoticeForm(forms.ModelForm):
    class Meta:
        model=Notice
        fields=['message']
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment 
        fields=['card_number','mobile_number','expiry_date','cvv','account_holder_name','amount_to_pay']
