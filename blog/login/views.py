from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from login.forms import *
from login.models import *

# Create your views here.

def login_in(request):
    
    if request.method == 'POST':
        user= authenticate(username= request.POST['username'], password= request.POST['password'])
        if user is not None:
            login(request, user)
            
            return render(request, 'one/index.html', {'inside':'ok'})
        else:
            return render(request, 'pages/login.html',{'err': 'usuario o contraseña incorrecto'})
    else:
        return render( request, 'pages/login.html')


def register(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate.is_valid():
            userCreate.save()
            return redirect('login')
        else:
            return render(request, 'pages/reglogin.html', {'err':'error'})    
    else:
        return render(request, 'pages/reglogin.html')

@login_required
def perfil(request):
    return render(request, 'pages/perfil/perfil.html')

@login_required
def updperfil(request, id_up):
    user = User.objects.get(pk=id_up)
    data= {"user": user}    
    return render(request, 'pages/perfil/updperfil.html', data)
    

@login_required
def updpass(request, id_up):
    user = User.objects.get(pk=id_up)
    data= {"user": user}    
    return render(request, 'pages/perfil/updpass.html', data)


@login_required
def useredicion(request, id_up):
    if request.method == "POST":
            username=request.POST["username"]
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
                            
            user = User.objects.get(pk=id_up)
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            
            user.save()
            return redirect('perfil')
    return redirect('perfil')
  
@login_required   
def passedicion(request, id_up):   
    if request.method == "POST":
        old_password=request.POST["password"]         
        user = User.objects.get(pk=id_up) 
        if user.password == old_password:        
            new_password1=request.POST["password1"]
            new_password2=request.POST["password2"]   
                    
            if new_password1 == new_password2:
                user = User.objects.get(pk=id_up)
                user.password = new_password1   
                user.save()
                return redirect('perfil')
            
    return redirect('perfil')

def updavatar(request):
    form= Avatar(request.POST, request.FILES)
    print(form)
    print(form.is_valid())
    if form.is_valid():
        user= User.objects.get(username= request.user)
        avatar=AvatarModel(user=user, image=form.cleaned_data['avatar'], id= request.user.id)
        avatar.save()
        avatar= AvatarModel.objects.filter(user= request.user.id)
        try:
            avatar=avatar[0].image.url
        except:
            avatar= None
        return render(request,'one/index.html',{'avatar':avatar})
    else:
        try:
            avatar =Avatar.objects.filter(user= request.user.id)
            form=Avatar()
        except:
            form=Avatar()
    return render(request,'pages/perfil/avatar.html',{'form':form})