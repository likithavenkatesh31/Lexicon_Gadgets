from django.shortcuts import render, redirect
from . import forms

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.

def userlogin(request):

    if request.method == 'POST':
        login_form = forms.UserLogin(data=request.POST)

        myusername = request.POST['username']
        mypassword = request.POST['password']

        user = authenticate(username=myusername,password=mypassword)
        print(user)
        # user = not None
        if user is not None:
            login(request, user)
            return render(request,'lexiconapp/login.html',{'user':user})
        else:
            print("error")

    else:
        login_form = forms.UserLogin()

    return render(request,'lexiconapp/login.html',{'login_form':login_form})