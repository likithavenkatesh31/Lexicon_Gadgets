from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from lexiconapp.models import *
from lexiconapp import forms
# Create your views here.


def index(request):
    return render(request, 'lexiconapp/base.html')


def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:

            messages.error(request, "Password does not Match,Please Try Again!")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request, "Username Already Exists")
                return redirect('/signup')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email Already Exists")
                return redirect('/signup')
        except Exception as identifier:
            pass
        # checks for error inputs
        user = User.objects.create_user(username, email, pass1)
        user.save()
        messages.info(request, 'Thanks For Signing Up')
        # messages.info(request,"Signup Successful Please Login")
        return redirect('/login')
    return render(request, "lexiconapp/signup.html")


# def signup(request):
#     registered = False
#     if request.method == 'POST':
#         form = UserForm(data=request.POST)

#         if form.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             user.save()
#             registered = True
#             return redirect('/login')

#         else:
#             print(form.errors)

#     else:
#         form = UserForm
#     return render(request, 'lexiconapp/signup.html',
#                   {'form': form,
#                    'registered': registered})


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

# @login_required
def orderconf(request):
    # need to take orderno from order model
    orderno = '1000'
    return HttpResponse("Your order is placed. order no {}".format(orderno))

# @login_required
def orderbyuser(request):

    pass


@login_required
def userlogout(request):
    logout(request)
    messages.success(request, 'logged out success')
    return redirect('userlogin')


def card(request):
    item_list = Product.objects.all().values()
    context = {'items': item_list, }
    return render(request, 'lexiconapp/card.html', context)


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if len(name) > 4 and len(phone) > 8 and len(phone) < 11 and len(message) > 2:
            messages.error(request, "Please fill the form correctly")
        else:
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.message = message
            contact.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, 'lexiconapp/contact.html')
