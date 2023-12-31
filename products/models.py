from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='media/')
    image_url = models.URLField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return self.name