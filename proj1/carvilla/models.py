from django.db import models

# Create your models here.
'''
class CarDescription():
    classid : int
    name : str
    img : str
    price: str
    description: str
    model: int
    miles : int
    horsepower: int
    auto: bool
'''

class CarDescription(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.TextField()
    description = models.TextField()
    model = models.IntegerField()
    kmph = models.IntegerField()
    horsepower = models.IntegerField()
    auto = models.BooleanField(default=False)