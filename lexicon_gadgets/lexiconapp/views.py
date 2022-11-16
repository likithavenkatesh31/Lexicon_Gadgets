from django.shortcuts import render, redirect
from lexiconapp import forms

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'lexiconapp/base.html')
def homepage(request):
    	return render(request, "lexiconapp/base.html")

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:homepage")
      
	form = forms.ContactForm()
	return render(request, "base/Contact.html", {'form':form})

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