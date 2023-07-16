"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from vistas.views import *
from login.views import *
from forms.views import *
from forms.models import *
from login.models import *

# admin.site.register(Users)
admin.site.register(Games)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home, name='home'),
    
    path('login/', login_in, name='login'),
    path('login/register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name= 'one/index.html'), name='logout'),
    
    path('perfil/', perfil, name='perfil'),
    path('perfil/datos/<id_up>', updperfil, name='updperfil'),
    path('perfil/password/', updpass, name='updpass'),
    path('perfil/avatar/', updavatar, name='updavatar'),
    path('perfil/datos/edicion/<id_up>', useredicion, name='useredicion'),
     
    path('ps/',ps, name='ps'),
    path('xbox/',xbox, name='xbox'),
    path('switch/',switch, name='switch'),
    path('pc/',pc, name='pc'),
    path('about/',about, name='about'),
    path('contenido/<int:id_up>/',contenido, name='contenido'),
    
    path('forms/',form, name='form'),
    path('forms/pslist/',pslist, name='pslist'),
    path('forms/delist/<id_del>',delist, name='delist'),
    path('forms/updform/<id_up>',updform, name='updform'),
    path('forms/updform/edicion/<id_up>',edicion, name='edicion'), 
]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)