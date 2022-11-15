from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def card(request):
  item_list = Product.objects.all().values()
  context = {'items': item_list,}
  return render(request,'lexiconapp/card.html',context)
    