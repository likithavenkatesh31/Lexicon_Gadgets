
from lexiconapp import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='base'),
    path('orderconf/', views.orderconf, name='orderconf'),
    path('logout/', views.userlogout, name='userlogout'),
    path('card', views.card, name='card'),
    path('lexiconapp/add/', views.add, name='add'),
    path('lexiconapp/add/addrecord/', views.addrecord, name='addrecord'),
    path('lexiconapp/delete/<int:id>', views.delete, name='delete'),
    path('lexiconapp/update/<int:id>', views.update, name='update'),
    path('lexiconapp/update/updaterecord/<int:id>',
         views.updaterecord, name='updaterecord'),
    path("signup", views.signup, name='signup'),
    path('orders/', views.orderbyuser, name='orders'),
    path('contact/', views.contact, name='contact'),
    
    
]
