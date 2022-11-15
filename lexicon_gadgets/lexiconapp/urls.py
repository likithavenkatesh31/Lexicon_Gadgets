

from django.urls import path
from  lexiconapp import views

urlpatterns = [
    #path('index/', views.index, name='index'),
    path('card',views.card, name='card'),
    
    
]
