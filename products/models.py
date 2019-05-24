from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your models here.

# Products
class Product(models.Model):
    category = models.CharField(max_length=100)
    part_name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=30)
    vehicle_model = models.CharField(max_length=35)
    required = models.DecimalField(max_digits=3, decimal_places=0)
    diagram_number = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user_ratings = models.ManyToManyField(UserProfile, through='UserRating', related_name="ratings")
    
    def __str__(self):
        return '{}: {}- {}'.format(self.category, self.part_name, self.part_number)
    
# Ratings
class UserRating(models.Model):
    class Meta:
        unique_together = ('product', 'user_profile')
    
    rating_choices = (
        ('disliked', 'Disliked'),
        ('liked', 'Liked')
    )
       
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ratings')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='product_ratings')
    rating = models.CharField(max_length=15, choices=rating_choices, null=True)