from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from checkout.models import *
from checkout.forms  import *
from django.db.models import F
from restaurant.models import fooditemdata
from .forms import *
from .models import Deliveryboydata
from deliveryboy.models import Deliveryboydata

# Create your views here.

def updatedelprofile(request,id):
    deldata1 = Deliveryboydata.objects.get(id=id)
    deldata = Deldataform(request.POST or None,request.FILES or None,instance =  deldata1)
    if request.method == "POST":
        if deldata.is_valid():
            deldata.save()
            return redirect("showdelprofile")
        else:
            print("error")
    context = {
        'deldata1': deldata1,
        'deldata': deldata,
    }
    return render(request, "deliveryboy/updatedelprofile.html", context)
    
    

def delsidebar(request):
    return render(request,"deliveryboy/delsidebar.html",)
    

def delhomepage(request):
    return render(request,"deliveryboy/delhomepage.html",)
    
    
def delreg(request):
    if request.method == 'POST':
        form = DelRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('dellogin')
    else:
        form = DelRegForm()
    return render(request,"deliveryboy/delreg.html",{"form":form})


def dellogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('deldashboard')
        else:
            return render(request, 'deliveryboy/dellogin.html', {'error': "! Invalid Password Or Email"})
    return render(request,"deliveryboy/dellogin.html",)


def dellogout(request):
    logout(request)
    return redirect('delhomepage')



from django.db.models import Q, F

def delorders(request):
    orders = Order.objects.filter(Q(delivery_order_choice='Select')).order_by(F('time').desc())
    rejected_orders = Order.objects.filter(delivery_order_choice='Reject').order_by('-time')
    accepted_orders = Order.objects.filter(delivery_order_choice='Accept').order_by('-time')
    context = {
        'orders':orders,
        'rejected_orders':rejected_orders,
        'accepted_orders':accepted_orders,
    }
    return render(request,"deliveryboy/orders.html",context)


def moreorderdetail(request,id):
    ordersdata = Order.objects.filter(id=id)
    restaurant = Restaurant_data.objects.all()
    context = {
        'ordersdata': ordersdata,
        # 'restdata': restdata,
        'restaurant': restaurant,
    }
    return render(request,"deliveryboy/moreorderdetails.html",context)

def deldashboard(request):
    current_user = request.user.id
    # orders = Order.objects.filter(restaurant_id=current_user).order_by(F('time').desc())
    orders = Order.objects.all()
    accepted_orders = Order.objects.filter(delivery_order_choice='Accept').order_by('-time')
    rejected_orders = Order.objects.filter(delivery_order_choice='Reject').order_by('-time')
    delivery_status = Order.objects.filter(delivery_status='Going To Restaurant').order_by('-time')
    delivery_status2 = Order.objects.filter(delivery_status='Picked Up').order_by('-time')
    delivery_status3 = Order.objects.filter(delivery_status='Delivered').order_by('-time')
    context = {
        'orders': orders,
        # 'fooddata': fooddata,
        # 'pending_orders':pending_orders,
        'accepted_orders':accepted_orders,
        'rejected_orders':rejected_orders,
        'delivery_status':delivery_status,
        'delivery_status2':delivery_status2,
        'delivery_status3':delivery_status3,
        
        # 'preparing_orders':preparing_orders,
        # 'ready_orders':ready_orders,
    }
    return render(request,"deliveryboy/deldashbord.html",context)


def showdelprofile(request):
    current_user = request.user
    showdata = Deliveryboydata.objects.filter(user__id=request.user.id)
    return render(request,"deliveryboy/showdelprofile.html",{'deldata1': showdata})

def updateorders(request, id):
    data1 = Order.objects.get(id=id)
    data = DelOrderChoice(request.POST or None, request.FILES or None, instance=data1)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect("delorders")
        else:
            print("errors")
            print(data.errors)
    return render(request, "deliveryboy/updateorders.html", {'data': data})

def updatedelstatus(request, id):
    data1 = Order.objects.get(id=id)
    data = DeliveryStatusForm(request.POST or None, request.FILES or None, instance=data1)
    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect("acceptedorder")
        else:
            print("errors")
            print(data.errors)
    return render(request, "deliveryboy/updatedelstatus.html", {'data': data})

def acceptedorder(request):
    ordersdata = Order.objects.filter(delivery_order_choice="Accept")
    return render(request,"deliveryboy/acceptedorder.html",{"ordersdata":ordersdata})
    
def rejectedorder(request):
    ordersdata = Order.objects.filter(delivery_order_choice="Reject")
    return render(request,"deliveryboy/rejectedorder.html",{"ordersdata":ordersdata})
    


    