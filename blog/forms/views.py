from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from forms.models import *

# Create your views here.

@login_required
@permission_required('forms.can_delete')
def form(request):
    if request.method == "POST":
        gamebd = Games(nombre=request.POST["nombre"],
                       descripcion=request.POST["descripcion"],
                       precio=request.POST["precio"],
                       stock=request.POST["stock"],
                       plataforma=request.POST["plataforma"]
                       )
        gamebd.save()
        return render(request, 'folders/form.html')
    return render(request, 'folders/form.html')


@login_required
def pslist(request):
    games = Games.objects.all()
    return render(request, 'folders/pslist.html', {'games': games})


@login_required
def delist(request, id_del):
    games = Games.objects.get(pk=id_del)
    games.delete()
    games = Games.objects.all()
    return render(request, 'folders/pslist.html', {'games': games})


@login_required
def updform(request, id_up):
    games = Games.objects.get(pk=id_up)
    data= {"games": games}
    return render(request, 'folders/updform.html', data)


@login_required
def edicion(request, id_up):
    if request.method == "POST":
            nombre=request.POST["nombre"]
            descripcion=request.POST["descripcion"]
            precio=request.POST["precio"]
            stock=request.POST["stock"]
            plataforma=request.POST["plataforma"]
                            
            gamebd = Games.objects.get(id=id_up)
            gamebd.nombre = nombre
            gamebd.descripcion = descripcion
            gamebd.precio = precio
            gamebd.stock = stock
            gamebd.plataforma = plataforma
            gamebd.save()
            return redirect('pslist')
    return redirect('pslist')