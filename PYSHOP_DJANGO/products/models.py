from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_stock = models.IntegerField()
    product_image_url = models.CharField(max_length=2083)


class Offers(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=2083)
    discount = models.IntegerField()


