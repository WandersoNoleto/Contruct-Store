from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name       = models.CharField(max_length=40)
    category   = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)
    amount     = models.FloatField()
    price_buy  = models.FloatField()
    price_sell = models.FloatField()

    def generate_discount(self, discount):
        return self.price_sell - ((self.price_sell * discount)/100)

    def profit(self):
        profit = self.price_sell - self.price_buy
        profit_percent = (profit*100)/self.price_buy

        return profit_percent   


    def __str__(self) -> str:
        return self.name



class Image(models.Model):
    image   = models.ImageField(upload_to="image_product")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

