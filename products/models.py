from django.db import models

# Create your models here.
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
   
    #def __str__(self):
        #return self.part_name
        #return '%s, %s, %s' % (self.category, self.part_name, self.part_number)
