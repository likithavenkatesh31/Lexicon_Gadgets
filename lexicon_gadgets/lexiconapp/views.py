from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from lexiconapp import forms
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'lexiconapp/base.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.warning(request, "Password is not matching")
            return render(request, 'lexiconapp/signup,html')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "Uername is taken")
                return render(request, 'lexiconapp/signup,html')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "This Email is already registered")
                return render(request, 'lexiconapp/signup,html')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username.email, password)
        myuser.save()
        messages.info(request, "Signup Successfull! Plese Login")
        return redirect('lexicon_app/index')
    return render(request, 'lexiconapp/signup.html')


# Create your views here.


# @login_required
# def user_logout(request):
#     logout(request)
#     return render(request, 'lexiconapp/base.html')


def userlogin(request):

    if request.method == 'POST':
        login_form = forms.UserLogin(data=request.POST)

        myusername = request.POST['username']
        mypassword = request.POST['password']

        user = authenticate(username=myusername, password=mypassword)
        print(user)
        # user = not None
        if user is not None:
            login(request, user)
            return render(request, 'lexiconapp/login.html', {'user': user})
        else:
            print("error")

    else:
        login_form = forms.UserLogin()

    return render(request, 'lexiconapp/login.html', {'login_form': login_form})
