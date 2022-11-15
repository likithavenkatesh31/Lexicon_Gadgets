from lexiconapp import views
from django.urls import path



urlpatterns = [
    # path('index/', views.index, name='index'),
    path('login/',views.userlogin, name='userlogin'),
    path('orderconf/', views.orderconf, name='orderconf'),
    path('logout/', views.userlogout, name='userlogout'),
]
