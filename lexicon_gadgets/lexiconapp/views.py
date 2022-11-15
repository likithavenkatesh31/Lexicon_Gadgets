from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'lexicon_app/base.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.warning(request, "Password is not matching")
            return render(request, 'lexicon_app/signup,html')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "Uername is taken")
                return render(request, 'lexicon_app/signup,html')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "This Email is already registered")
                return render(request, 'lexicon_app/signup,html')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username.email, password)
        myuser.save()
        messages.info(request, "Signup Successfull! Plese Login")
        return redirect('lexicon_app/index')
    return render(request, 'lexicon_app/signup.html')
