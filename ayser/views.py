from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'ayser/home.html')

def economy(request):
    return render(request, 'ayser/canadian_economy.html')

def kakeibo(request):
    return render(request, 'ayser/kakeibo.html')
