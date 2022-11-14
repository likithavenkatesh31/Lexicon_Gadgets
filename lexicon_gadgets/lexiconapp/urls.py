
from . import views
from django.urls import path
from django.conf.urls import url,include


urlpatterns = [
    path('index/', views.index, name='index'),
    # url(r'^basic_app/',include('basic_app.urls'))
]
