from django.db import models


from Admin.models import *
# Create your models here.
class District(models.Model):
    district_name=models.CharField(max_length=50)
    def __str__(self):
        return self.district_name  
        
class Place(models.Model):
    place_name=models.CharField(max_length=50)     
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name
class Category(models.Model):
    category_name=models.CharField(max_length=50)    
    def __str__(self):
        return self.category_name                

class SubCategory(models.Model):
    subcat_name=models.CharField(max_length=50)     
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self): 
        return self.subcat_name

class Product(models.Model):
    product_name=models.CharField(max_length=50)     
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    product_photo=models.FileField(upload_to='ProductDocs/')
    product_des=models.CharField(max_length=50)
    product_price=models.CharField(max_length=50)
    stock_qty=models.IntegerField(default=0)






 

  
# Create your models here.
