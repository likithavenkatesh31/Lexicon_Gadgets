from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
            title= models.CharField(max_length=255)
            description= models.CharField(max_length=255)
            price=  models.FloatField()
            brand= models.CharField(max_length=255)
            category= models.CharField(max_length=255)
            images= models.URLField(max_length=255)
            def __str__(self):
                    return self.title
            
            
            
            
            
# class Basket(models.Model):
#             user = models.ForeignKey(User, on_delete=models.CASCADE)
#             product = models.ForeignKey(Product, on_delete=models.CASCADE)
#             quantity=models.IntegerField()
#             pass
#             def __str__(self):
#                     return self.title
    
    

# class Oreder(models.Model):
    
#             order_number=models.IntegerField()
#             products = models.ManyToManyField(Basket)
#             ordered = models.BooleanField(default=False)
#             user = models.ForeignKey(User, on_delete=models.CASCADE)
#             start_date = models.DateTimeField(auto_now_add=True)
#             oredered_date=models.DateTimeField()
#             user_discount=models.DecimalField()
#             total_price=models.IntegerField()
#             def __str__(self):
#                     return self.user.username
            
    
    


           

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')




class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=240)
	email = models.CharField(max_length=240,unique=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)