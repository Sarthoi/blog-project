from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from login.forms import *
from login.models import *

# Create your views here.


def login_in(request):

    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            avatar = getavatar(request)
            return render(request, 'one/index.html',{'avatar': avatar})
        else:
            return render(request, 'pages/login.html', {'err': 'usuario o contraseña incorrecto'})
    else:
        return render(request, 'pages/login.html')


def register(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate.is_valid():
            userCreate.save()
            return redirect('login')
        else:
            return render(request, 'pages/reglogin.html', {'err': 'error'})
    else:
        return render(request, 'pages/reglogin.html')


@login_required
def perfil(request):
    avatar = getavatar(request)
    return render(request, 'pages/perfil/perfil.html',{'avatar': avatar})


@login_required
def updperfil(request, id_up):
    avatar = getavatar(request)
    user = User.objects.get(pk=id_up)
    data = {"user": user,"avatar": avatar}  
    return render(request, 'pages/perfil/updperfil.html', data)


@login_required
def updpass(request):
    usuario = request.user    
    avatar = getavatar(request)
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect( 'perfil')
        return render(request,'pages/perfil/updpass.html', {"form": form ,"avatar": avatar})
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, 'pages/perfil/updpass.html', {"form": form ,"avatar": avatar})


@login_required
def useredicion(request, id_up):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        user = User.objects.get(pk=id_up)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()
        return redirect('perfil')
    return redirect('perfil')


@login_required
def updavatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            avatar = AvatarModel(user=user, image=form.cleaned_data['avatar'], id=request.user.id)
            avatar.save()
            avatar = AvatarModel.objects.filter(user=request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'one/index.html', {'avatar': avatar})
    else:
        try:
            avatar = AvatarModel.objects.filter(user=request.user.id)
            form = AvatarForm()
            avatar = getavatar(request)
        except:
            avatar = getavatar(request)
            form = AvatarForm()
    return render(request, 'pages/perfil/avatar.html', {'form': form, 'avatar': avatar})

@login_required
def getavatar(request):
    avatar = AvatarModel.objects.filter(user=request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar
