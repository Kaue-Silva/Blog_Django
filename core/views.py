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
    request.user = str(request.user)
    dados = {'dados':publicacoes}
    return render(request, 'index.html', dados)

@login_required(login_url="/login/")
def tela_postagem(request):
    id_postagem = request.GET.get('id')
    dados = {}
    if id_postagem:
        dados['postagem'] = Postagem.objects.get(id=id_postagem)
    return render(request, 'postagem.html', dados)


@login_required(login_url="/login/")
def nova_postagem(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        publico = request.POST.get('publico')
        autor = request.user
        id_postagem = request.POST.get('id_postagem')
        if titulo == '' or titulo == None:
            titulo = 'Sem Titulo'
        
        if publico == 'on':
            publico = True
        
        else:
            publico = False
        
        if id_postagem:
            postagem = Postagem.objects.get(id=id_postagem)
            if postagem.autor == autor:
                postagem.titulo = titulo
                postagem.descricao = descricao
                postagem.publico = publico
                postagem.save()
        else:
            Postagem.objects.create(titulo=titulo, descricao=descricao, publico=publico, autor=autor)

    return redirect('/')

@login_required(login_url="/login/")
def postagens_listadas(request):
    autor = request.user
    postagens = Postagem.objects.filter(autor=autor, publico=False)
    dados = {"dados":postagens}
    return render(request, "postagens_listadas.html", dados)


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


@login_required(login_url="/login/")
def minhas_postagens(request):
    usuario = request.user
    postagens = Postagem.objects.filter(autor=usuario)
    dados = {"dados":postagens}
    return render(request, "minhas_postagens.html", dados)


@login_required(login_url="/login/")
def delete_postagem(request, id_postagem):
    usuario = request.user
    postagem = Postagem.objects.filter(autor=usuario, id=id_postagem)
    postagem.delete()
    return redirect('/blog/minhaspostagens/')