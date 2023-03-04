
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from .forms import SignUpForm,customer_extra_fields


class UserView(DetailView):
    template_name = 'account/profile.html'

    def get_object(self):
        return self.request.user


def signup(request):
    form = SignUpForm(request.POST)
    data = customer_extra_fields(request.POST)
    context = {
    'data':data,
    'form':form
    }
    if form.is_valid() and data.is_valid():
        user = form.save()
        user1 = data.save()
        password = form.cleaned_data.get('password1')
        user = authenticate(request, email=user.email, password=password)
        if user is not None:
            login(request,user)
        else:
            print("user is not authenticated")
        return redirect('custbase')
    else:
        form = SignUpForm()
        data = customer_extra_fields()
    return render(request, 'signup.html', context)
    