
from lexiconapp import views
from django.urls import path



urlpatterns = [
    #path('index/', views.index, name='index'),
    path('card',views.card, name='card'),
    
    
    path('', views.index, name='index'),
    path("signup", views.signup, name='signup'),
    # path('login',views.user_logout, name='logout'),
]
