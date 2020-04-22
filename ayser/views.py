from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'ayser/home.html')

def canadian_economy(request):
    return render(request, 'ayser/canadian_economy.html')

def kakeibo(request):
    return render(request, 'ayser/kakeibo.html')

def uw_placement_quiz(request):
    return render(request, 'ayser/uw_placement_quiz.html')

def uw_placement_quiz(request):
    return render(request, 'ayser/uw_engineering_program_classifier.html')
