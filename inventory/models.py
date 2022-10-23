from unicodedata import name

from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name       = models.CharField(max_length=40, unique=True)
    category   = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    amount     = models.FloatField()
    price_buy  = models.FloatField()
    price_sell = models.FloatField()
    slug       = models.SlugField(unique=True, blank=True, null=True)


    def generate_discount(self, discount):
        return self.price_sell - ((self.price_sell * discount)/100)


    def profit(self):
        profit = self.price_sell - self.price_buy
        profit_percent = (profit*100)/self.price_buy

        return profit_percent   


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.name



class Image(models.Model):
    image   = models.ImageField(upload_to="image_product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

