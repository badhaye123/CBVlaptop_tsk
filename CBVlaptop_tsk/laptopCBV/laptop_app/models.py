from django.db import models

# Create your models here.
class Laptop(models.Model):
    laptop_name=models.CharField(max_length=32)
    laptop_Manufacturer=models.CharField(max_length=32)
    RAM=models.IntegerField()
    ROM=models.IntegerField()
    weight=models.IntegerField()
    processor=models.CharField(max_length=32)
    price=models.FloatField()


    def __str__(self):
        return self.laptop_name
