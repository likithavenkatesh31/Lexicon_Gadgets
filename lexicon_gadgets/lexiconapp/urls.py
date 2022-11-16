
from . import views
from django.urls import path
from django.conf.urls import url,include
from . import views

app_name = "lexiconapp"



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('lexiconapp.urls')),
    path("contact", views.contact, name="contact"),
    
]




