from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.title
