from django.shortcuts import render,redirect,HttpResponse
from .forms  import orderform
from cart.cart import Cart
from .models import Order
from accounts.models import User
# from restaurant.models import fooditemdata
from django.views.decorators.csrf import csrf_exempt

def CheckOut(request):
    orderdata = orderform(request.POST)
    if request.method == "POST":
        first_name = request.POST.get("first_name")    
        last_name = request.POST.get("last_name")    
        address = request.POST.get("address")    
        state = request.POST.get("state")
        city = request.POST.get("city")    
        area = request.POST.get("area")    
        order_total = request.POST.get("order_total")    
        phone_number = request.POST.get("phone_number")    
        pin_code = request.POST.get("pin_code")  
        cart = request.session.get('cart')
        uid = request.session.get("_auth_user_id")
        user = User.objects.get(pk=uid)
        
        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b
            print(i)
            order = Order(
                user = user,
                f_name = cart[i]['name'],
                restaurant_id = cart[i]['restaurant'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                first_name = first_name,
                last_name = last_name,
                address = address,
                state = state,
                city = city,
                area = area,
                phone_number = phone_number,
                pin_code = pin_code,
                total = total,
                order_total=order_total
            )
            order.save()
        print(cart)
        request.session['cart'] = {}
        return redirect("custhomepage")
        # if order.is_valid():
        # else:
        #     print('error')
    return render(request, "customer/checkout.html", {'orderdata': orderdata})


@csrf_exempt
def handlerequest(request):
    pass