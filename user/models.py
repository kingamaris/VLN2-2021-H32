from django.db import models


class Category(models.Model):
    """
    Category Model represents a specific product category
    """
    name = models.CharField(max_length=300, unique=True)


class Product(models.Model):
    """
    Product Model represents a single product
    """
    name = models.CharField(max_length=300)
    supplier = models.CharField(max_length=300)
    description = models.TextField(max_length=9000)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Keyword(models.Model):
    """
    Keyword Model contains a descriptive keyword and the product it describes
    """
    name = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductPhoto(models.Model):
    """
    ProductPhoto Model contains a url to a photo of a product and the product itself.
    """
    url = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)