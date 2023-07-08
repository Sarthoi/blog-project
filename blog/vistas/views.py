from django.shortcuts import render
from forms.models import *

# Create your views here.

def home(request):
    return render(request, 'one/index.html')

def ps(request):
    games= Games.objects.all()
    return render(request, 'one/playstation.html', {"games": games})

def xbox(request):
    games= Games.objects.all()
    return render(request, 'one/xbox.html' , {"games": games})

def switch(request):
    games= Games.objects.all()
    return render(request, 'one/switch.html' , {"games": games})

def pc(request):
    games= Games.objects.all()
    return render(request, 'one/pc.html' , {"games": games})

    