
from django.db import models    
# Create your models here.




class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.title



class noisemap(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.FloatField()
    # def __str__(self):
    #     return str(self.x)


class grade_cbc(models.Model):
    a1 = models.ImageField()
    a2 = models.ImageField()
    a3 = models.ImageField()
    a4 = models.ImageField()
    a5 = models.ImageField()
    a6 = models.ImageField()
    a7 = models.ImageField()
    a8 = models.ImageField()
    a9 = models.ImageField()
    a10 = models.ImageField()
    a11 = models.ImageField()
    a12 = models.ImageField()
    a13 = models.ImageField()
    a14 = models.ImageField()
    a15 = models.ImageField()
    

    
    
   
                        
