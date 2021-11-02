from django.shortcuts import redirect, render
from core.models import Postagem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def tela_login(request):
    return render(request, 'login.html')


def login_conta(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou Senha, Estão incorretos.")
    
    return redirect('/')


@login_required(login_url='/login/')
def sair(request):
    logout(request)
    return redirect('/')



def index(request):
    publicacoes = Postagem.objects.all()
    usuario = request.user
    dados = {'dados':publicacoes, 'usuario':usuario}
    return render(request, 'index.html', dados)

@login_required(login_url="/login/")
def tela_postagem(request):
    return render(request, 'postagem.html')

@login_required(login_url="/login/")
def nova_postagem(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        publico = request.POST.get('publico')
        autor = request.user
        if titulo == '' or titulo == None:
            titulo = 'Sem Titulo'
        if publico == 'on':
            publico = True
        else:
            publico = False
        Postagem.objects.create(titulo=titulo, descricao=descricao, publico=publico, autor=autor)

    return redirect('/')

@login_required(login_url="/login/")
def minhas_postagens(request):
    autor = request.user
    postagens = Postagem.objects.filter(autor=autor, publico=False)
    dados = {"dados":postagens, 'usuario':autor}
    return render(request, "minhas_postagens.html", dados)


def registrar(request):
    if request.POST:
        try:
            usuario = request.POST.get('username')
            senha = request.POST.get('password')
            user = User.objects.create_user(username=usuario, password=senha)
            messages.success(request=request, message="Registro Completo.")
            return redirect('/')
        except:
            messages.error(request=request, message="Usuario ja existe.")
            return redirect('/')