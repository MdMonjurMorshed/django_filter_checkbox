from django.db import models
from .abstruct import *

# Create your models here.
class Category(CommonFields):
    title=models.CharField(max_length=50,blank=False)


    def __str__(self) :
        return self.title

class Brand(CommonFields):
    title=models.CharField(max_length=50,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return self.title +'-' +self.category.title
class Warrenty(CommonFields):
    title=models.CharField(max_length=50,blank=False)

    def __str__(self) -> str:
        return self.title
    
class Seller(CommonFields):
    shop_name=models.CharField(max_length=100,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.shop_name +'-' + self.brand.title +'-'+  self.category.title

class Product(CommonFields):
    title=models.CharField(max_length=100,blank=False)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    warrenty=models.ForeignKey(Warrenty,on_delete=models.CASCADE,null=True,blank=True)
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE,null=True,blank=True)
    product_image=models.ImageField(upload_to='product_image',null=True,blank=True)

    def __str__(self) -> str:
        return self.title


