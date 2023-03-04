from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile
from restaurant.models import Restaurant_data
from deliveryboy.models import Deliveryboydata

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_customer:
        Profile.objects.create(user=instance)
    elif created and instance.is_restaurantowner:
        try:
            Restaurant_data.objects.create(user=instance)
        except Exception as e:
            print(f"Error creating Restaurant_data instance: {e}")
    elif created and instance.is_deliveryboy:
        try:
            Deliveryboydata.objects.create(user=instance)
        except Exception as e:
            print(f"Error creating Deliveryboydata instance: {e}")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_customer:
        try:
            instance.profile.save()
        except Exception as e:
            print(f"Error saving Profile instance: {e}")
    elif instance.is_restaurantowner:
        try:
            instance.restaurant_data.save()
        except Exception as e:
            print(f"Error saving Restaurant_data instance: {e}")
    elif instance.is_deliveryboy:
        try:
            instance.Deliveryboydata.save()
        except Exception as e:
            print(f"Error saving Deliveryboydata instance: {e}")
















# from accounts.models import *
# from django.shortcuts import render, redirect

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Profile
# from restaurant.models import *
# from deliveryboy.models import *

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.is_customer:
#         Profile.objects.create(user=instance)
#     elif instance.is_restaurantowner:
#             Restaurant_data.objects.create(user=instance)
#     elif instance.is_deliveryboy:
#         Deliveryboydata.objects.create(user=instance)
        
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_customer:
#         instance.profile.save()
#     elif instance.is_restaurantowner:
#         instance.restaurant_data.save()
#     elif instance.is_deliveryboy:
#         instance.deliveryboy_data.save()