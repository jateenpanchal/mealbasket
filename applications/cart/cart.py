from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from restaurant.models import fooditemdata


class Cart(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, fooditemdata, quantity=1, action=None):
        """
        Add a fooditemdata to the cart or update its quantity.
        """
        id = fooditemdata.id
        newItem = True
        if str(fooditemdata.id) not in self.cart.keys():

            self.cart[fooditemdata.id] = {
                'fooditemdata_id': fooditemdata.id,
                'name': fooditemdata.food_name,
                'quantity': 1,
                'price': str(fooditemdata.food_price),
                'image': fooditemdata.food_photo.url,
                'restaurant': fooditemdata.user.id,
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(fooditemdata.id):

                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[fooditemdata.id] = {
                    'userid': self.request,
                    'fooditemdata_id': fooditemdata.id,
                    'name': fooditemdata.food_name,
                    'quantity': 1,
                    'price': str(fooditemdata.food_price),
                    'image': fooditemdata.image.url,
                    'restaurant': fooditemdata.user.id,
                }

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, fooditemdata):
        """
        Remove a fooditemdata from the cart.
        """
        fooditemdata_id = str(fooditemdata.id)
        if fooditemdata_id in self.cart:
            del self.cart[fooditemdata_id]
            self.save()

    def decrement(self, fooditemdata):
        for key, value in self.cart.items():
            if key == str(fooditemdata.id):

                value['quantity'] = value['quantity'] - 1
                if (value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
