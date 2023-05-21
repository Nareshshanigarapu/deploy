from django.db import models

# Create your models here.
class wine_shop(models.Model):
    brand_name=models.CharField(max_length=50)
    brand_dis=models.CharField(max_length=50)
    brand_rate=models.IntegerField()
    brand_type=models.CharField(max_length=20)