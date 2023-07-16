from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email= forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Correo'}))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'contraseña'}))
    
    class Meta:
        model=User
        fields= ['username', 'email', 'first_name','last_name', 'password']
        help_texts={k:'' for k in fields}
        
class ChangePasswordForm(PasswordChangeForm):
    old_password= forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña actual'}))
    new_password1= forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese nueva contraseña'}))
    new_password2= forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repita nueva contraseña'}))
    
    class Meta:
        model= User
        fields=['old_password', 'new_password1', 'new_password']
        help_texts={k:'' for k in fields}

class AvatarForm(forms.Form):
    avatar= forms.ImageField()