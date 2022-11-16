from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,permission_required
from lexiconapp.models import UserForm,Product
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

    return render(request,'lexiconapp/login.html',{'login_form':login_form})

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
    messages.success(request,'logged out success')
    return redirect('userlogin')
    
def card(request):
  item_list = Product.objects.all().values()
  context = {'items': item_list,}
  return render(request,'lexiconapp/card.html',context)
    

