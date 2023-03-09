from django.shortcuts import render
from django.http import HttpResponse 
from myapp.models import Dostavka


def all_product(request):
    products = Dostavka.objects.all().order_by('-id')

    context = {
        'products':products,
    }

    return render(request, "all_product.html", context)

def completed_product(request):
    products = Dostavka.objects.filter(status='yetkazib berilgan').order_by('-id')

    context = {
        'products':products,
    }
    return render(request, "complated_product.html", context)



def waiting_product(request):
    products = Dostavka.objects.filter(status='tayyorlanyabdi').order_by('-id')

    context = {
        'products':products,
    }
    return render(request, "waiting_product.html", context)