from django.shortcuts import render
from forms.models import *

# Create your views here.

def psform(request):
    if request.method == "POST":
        gamebd= Games (nombre=request.POST["nombre"],
                        descripcion=request.POST["descripcion"],
                        precio=request.POST["precio"],
                        stock=request.POST["stock"],
                        plataforma=request.POST["plataforma"]
                        )
        gamebd.save()
        return render(request, 'folders/psform.html')
    return render(request, 'folders/psform.html')