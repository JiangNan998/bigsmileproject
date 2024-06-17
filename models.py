from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    title = models.CharField(null=True,blank=True,max_length=50)
    logo = models.ImageField(upload_to='logo/',null=True,blank=True)
    def __str__(self):
        return self.title


#产品分类
class Classes(models.Model):
    text = models.CharField(max_length=50)
    def __str__(self):
        return self.text

#产品
class Productinfo(models.Model):
    productTitle = models.CharField(max_length=50)
    productImg = models.ImageField(upload_to='productinfo/', null=True,blank=True)
    belong = models.ForeignKey(Classes,on_delete=models.SET_NULL,related_name='productinfo_classes',
    null=True,blank=True)
    def __str__(self):
        return self.productTitle

#product详情页
class Product(models.Model):
    productinfo = models.ForeignKey(Productinfo, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Productinfo/',null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title