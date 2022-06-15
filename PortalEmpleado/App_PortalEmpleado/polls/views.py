from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacantes

def home(request):
    return render(request, 'home.html')
