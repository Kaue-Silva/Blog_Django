"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.tela_login),
    path('login/submit', views.login_conta),
    path('login/register', views.registrar),
    path('blog/', views.index),
    path('', RedirectView.as_view(url='blog/')),
    path('blog/logout/', views.sair),
    path('blog/novo/', views.tela_postagem),
    path('blog/novo/submit', views.nova_postagem),
    path('blog/postagens/', views.postagens_listadas),
    path('blog/minhaspostagens/', views.minhas_postagens),
    path('blog/minhaspostagens/delete/<int:id_postagem>', views.delete_postagem)

]
