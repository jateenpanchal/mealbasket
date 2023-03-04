from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from mealbasketapp.models import category
from checkout.models import *
from checkout.forms  import *
from django.db.models import F



# # Create your views here.


# Restaurant Registration
def restreg(request):
    if request.method == 'POST':
        form = RestRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email,
                                password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('restlogin')
    else:
        form = RestRegForm()
    return render(request, 'restaurant/restreg.html', {'form': form})


# Restaurant Login
def restlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('restdashbord')
        else:
            return render(request, 'restaurant/restlogin.html', {'error': "! Invalid Username,Password Or Email"})
    return render(request, "restaurant/restlogin.html")


# Restaurant Logout
def restlogout(request):
    logout(request)
    return redirect('resthomepage')


# Restaurant Food Item add
@login_required(login_url='restlogin')
def addfooditem(request):
    form = fooditemdataform(request.POST, request.FILES)
    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("restfoodmenu")
    else:
        print("_____________________________errorr____________________________")
        return render(request, "restaurant/addfooditem.html", {'fooddata': form})



# Add Restaurant Personal Data
def Restaurantdata(request):
    restdata = restdataform(request.POST)
    if request.method == "POST":
        Restaurant_Name = request.POST.get("Restaurant_Name")    
        Restaurant_Email = request.POST.get("Restaurant_Email")    
        Restaurant_Type = request.POST.get("Restaurant_Type")    
        Restaurant_Address = request.POST.get("Restaurant_Address")    
        Restaurant_GSTno = request.POST.get("Restaurant_GSTno")    
        uid = request.session.get("_auth_user_id")
        user = User.objects.get(pk=uid)
        
        restaurant_data = Restaurant_data(
            user = user,
            Restaurant_Name =Restaurant_Name,
            Restaurant_Email = Restaurant_Email,
            Restaurant_Type = Restaurant_Type,
            Restaurant_Address = Restaurant_Address,
            Restaurant_GSTno = Restaurant_GSTno
        )
        restaurant_data.save()
        return redirect("resthomepage")
        
        print(Restaurant_Name,Restaurant_Email,user,cart)
        
    return render(request, "restaurant/restdata.html", {"restdata": restdata})


def resthomepage(request):
    return render(request, "restaurant/resthomepage.html")


@login_required(login_url='restlogin')
def restfoodmenu(request):
    fooddata = fooditemdata.objects.filter(user__id=request.user.id)
    context = {
        'fooddata': fooddata,
    }
    return render(request,"restaurant/restfoodmenu.html",context)
    
def deletfooditem(request,id):
    data = fooditemdata.objects.get(id=id)
    if data:
        data.delete()
        return redirect("restfoodmenu")
    else:
        return render(request,'restwisefood.html')
    return render(request,'restwisefood.html')

def updatefooditem(request,id):
    data1 = fooditemdata.objects.get(id=id)
    data = fooditemdataform(request.POST or None,request.FILES or None,instance =  data1)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect("restfoodmenu")
        else:
            print("error")
    return render(request, "restaurant/updatefooditem.html", {'fooddata': data})

################################## ORDERS views ############################### 

def restupdateorders(request, id):
    data1 = Order.objects.get(id=id)
    data = OrderStatusForm(request.POST or None, request.FILES or None, instance=data1)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect("custorders")
        else:
            print("errors")
            print(data.errors)
    return render(request, "restaurant/updateorders.html", {'data': data})



def custorders(request):
    current_user = request.user.id
    orders = Order.objects.filter(restaurant_id=current_user).order_by(F('time').desc())
    return render(request,"restaurant/orders.html",{'orders':orders})   


def restprofile(request):
    restdata = restdataform(request.POST,request.FILES)
    if request.method == "POST" and restdata.is_valid():
        instance = restdata.save(commit=False)
        instance.user = request.user
        print(request.user)
        instance.save()
        return redirect("showuserprofile")
    else:
        print("_________________________________________________________________")
        return render(request, "customer/custdata.html", {'restdata': restdata})

def showrestprofile(request):
    current_user = request.user
    restdata1 = Restaurant_data.objects.filter(user__id=request.user.id)
    return render(request, "restaurant/showrestprofile.html", {'restdata1': restdata1})

def updaterestprofile(request,id):
    custdata1 = Restaurant_data.objects.get(id=id)
    custdata = restdataform(request.POST or None,request.FILES or None,instance =  custdata1)
    if request.method == "POST":
        if custdata.is_valid():
            custdata.save()
            return redirect("showrestprofile")
        else:
            print("error")
    context = {
        'custdata1': custdata1,
        'custdata': custdata,
    }
    return render(request, "restaurant/updaterestprofile.html", context)



from django.db.models import Q, F
def restdashbord(request):
    current_user = request.user.id
    orders = Order.objects.filter(restaurant_id=current_user).order_by(F('time').desc())
    pending_orders = Order.objects.filter(Q(restaurant_id=current_user) & Q(order_status='pending')).order_by(F('time').desc())
    accepted_orders = Order.objects.filter(restaurant_id=current_user,order_status='accepted').order_by('-time')
    preparing_orders = Order.objects.filter(restaurant_id=current_user,order_status='preparing').order_by('-time')
    ready_orders = Order.objects.filter(restaurant_id=current_user,order_status='ready').order_by('-time')
    fooddata = fooditemdata.objects.filter(user__id=request.user.id)
    
    
    # orders = Order.objects.filter(restaurant_id=current_user).order_by(F('time').desc())
    context = {
        'orders': orders,
        'fooddata': fooddata,
        'pending_orders':pending_orders,
        'accepted_orders':accepted_orders,
        'preparing_orders':preparing_orders,
        'ready_orders':ready_orders,
    }
    return render(request,"restaurant/restdashbord.html",context)