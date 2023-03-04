from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User
# from restaurant.models import *

# Create your models here.


r_types= (
    
    # ('Select','Select'),
    ('Veg','Veg'),
    ('Non-Veg','Non-Veg'),
    ('Both','Both'),

)

class Restaurant_data(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Restaurant_Name = models.CharField(max_length=100)
    Restaurant_Email = models.EmailField()
    Restaurant_Phoneno = models.CharField(max_length=10)
    Restaurant_Type = models.CharField(max_length=7,choices=r_types)
    Restaurant_Address = models.TextField()
    Restaurant_GSTno = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.Restaurant_Name
    

class fooditemdata(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category_name = models.ForeignKey("mealbasketapp.category", on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    food_price = models.CharField(max_length=5)
    food_photo = models.ImageField(upload_to='img/food_picture/')
    availability = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.food_name
