from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=99.99)

    def __str__(self):
        return str(self.title)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "20%"
