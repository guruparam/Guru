from django.db import models

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
    name = models.CharField(max_length=200,null=False,blank=False)
    released_year= models.DateField()
    available_quantities = models.IntegerField(null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available= models.BooleanField(default=False,help_text='available-default,outofstock-hidden')
    image = models.ImageField(upload_to="image1/",null=True,blank=True)     

    def __str__(self):
        return self.name