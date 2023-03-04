# from accounts.models import *
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import *

# def create_restaurant_data(sender, instance, created, **kwargs):
#     if created and instance.is_restaurantowner:
#         Restaurant_data.objects.create(user=instance)