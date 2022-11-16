
from lexiconapp import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='base'),
    path('orderconf/', views.orderconf, name='orderconf'),
    path('logout/', views.userlogout, name='userlogout'),
    path('card',views.card, name='card'),
    path("signup", views.signup, name='signup'),

    path('orders/', views.orderbyuser, name='orders'),


    path('contact/',views.contact, name='contact'),

]
