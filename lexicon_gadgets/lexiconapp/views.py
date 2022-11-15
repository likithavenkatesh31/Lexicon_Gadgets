from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from lexiconapp.models import UserForm
from lexiconapp import forms
# Create your views here.


def index(request):
    return render(request, 'lexiconapp/base.html')


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm

    return render(request, 'lexiconapp/signup.html',
                  {'user_form': user_form,
                   'registered': registered})


# Create your views here.


def card(request):
  item_list = Product.objects.all().values()
  context = {'items': item_list,}
  return render(request,'lexiconapp/card.html',context)
    
