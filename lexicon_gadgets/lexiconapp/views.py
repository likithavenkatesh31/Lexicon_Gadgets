from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from lexiconapp.models import UserForm,Product,Contact
from lexiconapp import forms
from .models import Product

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



from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.



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

@login_required
def userlogout(request):
    logout(request)
    messages.success(request,'logged out success')
    return redirect('userlogin')
    
def card(request):
  item_list = Product.objects.all().values()
  context = {'items': item_list,}
  return render(request,'lexiconapp/card.html',context)

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if len(name)>4  and len(phone)>8 and len(phone)<11 and len(message)>2:
            messages.error(request, "Please fill the form correctly")
        else:
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.message = message
            contact.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, 'lexiconapp/contact.html')
def homepage(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"lexiconapp/homepage.html", params )


        
        


