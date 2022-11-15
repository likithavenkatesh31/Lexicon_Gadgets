
from lexiconapp import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='base'),
    path('login/',views.userlogin, name='userlogin'),
    path('orderconf/', views.orderconf, name='orderconf'),
    path('logout/', views.userlogout, name='userlogout'),
    path("signup", views.signup, name='signup'),
]
