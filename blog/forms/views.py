from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from forms.models import *
from login.views import getavatar

# Create your views here.

@login_required
@permission_required('forms.can_delete')
def form(request):
    avatar = getavatar(request)
    if request.method == "POST":
        gamebd = Games(nombre=request.POST["nombre"],
                       descripcion=request.POST["descripcion"],
                       precio=request.POST["precio"],
                       stock=request.POST["stock"],
                       plataforma=request.POST["plataforma"],
                       imagen=request.FILES.get("imagen")
                       )
        gamebd.save()
        return render(request, 'folders/form.html',{'avatar': avatar})
    return render(request, 'folders/form.html',{'avatar': avatar})


@login_required
@permission_required('forms.can_delete')
def pslist(request):
    games = Games.objects.all()
    avatar = getavatar(request)
    return render(request, 'folders/pslist.html', {'games': games, 'avatar': avatar})


@login_required
@permission_required('forms.can_delete')
def delist(request, id_del):
    games = Games.objects.get(pk=id_del)
    games.delete()
    games = Games.objects.all()
    avatar = getavatar(request)
    return render(request, 'folders/pslist.html', {'games': games, 'avatar': avatar})


@login_required
@permission_required('forms.can_delete')
def updform(request, id_up):
    games = Games.objects.get(pk=id_up)
    avatar = getavatar(request)
    data= {"games": games, 'avatar': avatar}
    return render(request, 'folders/updform.html', data)


@login_required
@permission_required('forms.can_delete')
def edicion(request, id_up):
    if request.method == "POST":
            nombre=request.POST["nombre"]
            descripcion=request.POST["descripcion"]
            precio=request.POST["precio"]
            stock=request.POST["stock"]
            plataforma=request.POST["plataforma"]
            imagen=request.POST["imagen"]
                            
            gamebd = Games.objects.get(id=id_up)
            gamebd.nombre = nombre
            gamebd.descripcion = descripcion
            gamebd.precio = precio
            gamebd.stock = stock
            gamebd.plataforma = plataforma
            gamebd.imagen= imagen
            gamebd.save()
            return redirect('pslist')
    return redirect('pslist')