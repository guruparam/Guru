from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="image/",null=True,blank=True)

    def __str__(self):
        return self.name
    
class Phonemodel(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False,blank=False) # type: ignore
    released_year= models.DateField()
    available_quantities = models.IntegerField(null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available= models.BooleanField(default=False,help_text='available-default,outofstock-hidden')
    image = models.ImageField(upload_to="image1/",null=True,blank=True)     

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    model = models.ForeignKey(Phonemodel,on_delete=models.CASCADE)
    trans_choice = (
        ("card","card"),
        ("cash","cash"),
    )
    transaction_type = models.CharField(max_length=15,choices=trans_choice,default='cash')
    amount = models.IntegerField(null=False,blank=False)

    def __str__(self):
        return self.transaction_type