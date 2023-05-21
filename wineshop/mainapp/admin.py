from django.contrib import admin
from mainapp.models import wine_shop

class wineshop_admin(admin.ModelAdmin):
    list_display=['brand_name','brand_dis','brand_rate','brand_type']
admin.site.register(wine_shop,wineshop_admin)
# Register your models here.
