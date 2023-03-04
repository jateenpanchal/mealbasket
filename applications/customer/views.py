from cart.cart import Cart
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from .forms import userregform
from restaurant.models import fooditemdata
from mealbasketapp.models import category
from .forms import *
from cart.cart import Cart
from django.db.models import F

from checkout.models import Order
# Create your views here.


def my(request,id):
    custdata1 = Profile.objects.filter(id=id)
    return render(request,"customer/my.html",custdata1)


######################################### Reg , Login, Logout   ##################################


def custreg(request):
    if request.method == 'POST':
        form = CustRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('custlogin')
    else:
        form = CustRegForm()
    return render(request, 'customer/custreg.html', {'form': form})


def custlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('custhomepage')
        else:
            return render(request, 'customer/custlogin.html', {'error': "! Invalid Password Or Email"})
    return render(request, "customer/custlogin.html")


def custlogout(request):
    logout(request)
    return redirect('custhomepage')


################################### Reg , Login, Logout end ##################################

def index(request):
    catdata = category.objects.filter(category_status=True)
    custdata1 = Profile.objects.filter(Customer_Email=id)
    context = {
        'catdata': catdata,
        'custdata1':custdata1,
    }
    return render(request,'customer/cust_homepage.html',context)


def catwisefood(request, id):
    fooddata = fooditemdata.objects.filter(category_name=id)
    catdata = category.objects.all()
    context = {
        'fooddata': fooddata,
        'catdata': catdata,
    }
    return render(request, 'customer/catwisefood.html', context)


def foodcart(request):
    return render(request, "customer/foodcart.html")


def menu(request):
    
    
    # restdata = fooditemdata.objects.get(user=user)
    fooddata = fooditemdata.objects.filter(availability=True)
    catdata = category.objects.all()
    context = {
        'fooddata': fooddata,
        'catdata': catdata,
    }
    return render(request, "customer/menu.html", context)


@login_required(login_url='custlogin')
def contact(request):
    return render(request, 'customer/contact.html')

######################################### cart functionality   ##################################


@login_required(login_url="custlogin")
def cart_add(request, id):
    cart = Cart(request)
    product = fooditemdata.objects.get(id=id)
    cart.add(product)
    return redirect("menu")


@login_required(login_url="custlogin")
def item_clear(request, id):
    cart = Cart(request)
    product = fooditemdata.objects.get(id=id)
    cart.remove(product)
    return redirect("foodcart")


@login_required(login_url="custlogin")
def item_increment(request, id):
    cart = Cart(request)
    product = fooditemdata.objects.get(id=id)
    cart.add(product)
    return redirect("foodcart")


@login_required(login_url="custlogin")
def item_decrement(request, id):
    try:        
        cart = Cart(request)
        product = fooditemdata.objects.get(id=id)
        cart.decrement(product)
        return redirect("foodcart")
    except:
        return redirect("foodcart")
        


@login_required(login_url="custlogin")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("foodcart")


@login_required(login_url="custlogin")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


    ######################################### Profile   ##################################
    
def profilebase(request):
    useremail = User.objects.filter(email=request.user).first()
    userprofile = Profile.objects.filter(Customer_Email=useremail).first()
    context = {
        "useremail":useremail,
        "userprofile":userprofile,
        
    }
    return render(request,"customer/profilebase.html",context)

def custprofile(request):
    custdata = custdataform(request.POST,request.FILES)
    if request.method == "POST" and custdata.is_valid():
        instance = custdata.save(commit=False)
        instance.user = request.user
        print(request.user)
        instance.save()
        return redirect("showuserprofile")
    else:
        print("_________________________________________________________________")
        return render(request, "customer/custdata.html", {'custdata': custdata})

def showuserprofile(request):
    current_user = request.user
    custdata1 = Profile.objects.filter(user__id=request.user.id)
    return render(request, "customer/showuserprofile.html", {'custdata1': custdata1})


def updateuserprofile(request,id):
    custdata1 = Profile.objects.get(id=id)
    custdata = custdataform(request.POST or None,request.FILES or None,instance =  custdata1)
    if request.method == "POST":
        if custdata.is_valid():
            custdata.save()
            return redirect("showuserprofile")
        else:
            print("error")
    context = {
        'custdata1': custdata1,
        'custdata': custdata,
    }
    return render(request, "customer/updateuserprofile.html", context)
    
    
def customerorders(request):
    current_user = request.user
    custorders = Order.objects.filter(user=current_user).order_by(F('time').desc())
    return render(request,'customer/custorders.html',{'custorders':custorders})
    
    
def customerordersdetails(request,time):
    ordersdetails = Order.objects.filter(time=time).filter(user=request.user).first()
    return render(request,'customer/custorders.html')