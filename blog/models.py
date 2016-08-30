from django.db import models
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Product(models.Model):
    product_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image_file = models.ImageField()
    description = models.TextField(max_length=500)
    review = models.TextField(max_length=500, default="")
    Product_satisfaction_by11st = models.IntegerField(default=0)
    pricePos = models.IntegerField()
    priceNeg = models.IntegerField()
    deliveryPos = models.IntegerField()
    deliveryNeg = models.IntegerField()
    sizePos = models.IntegerField()
    sizeNeg = models.IntegerField()
    extraPos = models.IntegerField()
    extraNeg = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)