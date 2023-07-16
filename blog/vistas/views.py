from django.shortcuts import render
from forms.models import *
from login.views import getavatar

# Create your views here.

def home(request):
    avatar = getavatar(request)
    return render(request, 'one/index.html' ,{'avatar': avatar})

def about(request):
    avatar = getavatar(request)
    return render(request, 'one/about.html',{'avatar': avatar})

def ps(request):
    games= Games.objects.all()
    avatar = getavatar(request)
    return render(request, 'one/playstation.html', {"games": games, 'avatar': avatar})

def xbox(request):
    games= Games.objects.all()
    avatar = getavatar(request)
    return render(request, 'one/xbox.html' , {"games": games, 'avatar': avatar})

def switch(request):
    games= Games.objects.all()
    avatar = getavatar(request)
    return render(request, 'one/switch.html' , {"games": games, 'avatar': avatar})

def pc(request):
    games= Games.objects.all()
    avatar = getavatar(request)
    return render(request, 'one/pc.html' , {"games": games, 'avatar': avatar})

def contenido(request, id_up):
    g = Games.objects.get(pk=id_up)
    avatar = getavatar(request)
    data= {"g": g, 'avatar': avatar}
    return render(request, 'one/contenido.html', data)



    