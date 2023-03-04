from django.db import models
import datetime
# Create your models here.
from restaurant.models import fooditemdata
from mealbasketapp.models import category
from accounts.models import User
from restaurant.models import*
# Create your models here.

ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('preparing', 'Preparing'),
    ('ready', 'Ready for pickup'),
    # ('delivered', 'Delivered'),
)

DELIVERY_STATUS_CHOICES = (
    ('Going To Restaurant', 'Going To Restaurant'),
    ('Picked Up', 'Picked Up'),
    ('Delivered', 'Delivered'),
)
DELIVERY_ORDER_CHOICES = (
    ('Select', 'Select'),
    ('Accept', 'Accept'),
    ('Reject', 'Reject'),
)

class Order(models.Model):
    image = models.ImageField(upload_to='img/order/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant_id = models.CharField(max_length=100)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='Going To Restaurant')
    delivery_order_choice = models.CharField(max_length=20, choices=DELIVERY_ORDER_CHOICES, default='Select')
    f_name = models.CharField(max_length=100,default="")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    pin_code = models.CharField(max_length=6)
    quantity = models.CharField(max_length=5)
    price = models.IntegerField()
    total = models.CharField(max_length=1000,default="")
    order_total = models.CharField(max_length=1000,default="")
    date = models.DateField(default=datetime.datetime.today)
    time = models.DateTimeField(auto_now_add=True,auto_now=False)
    