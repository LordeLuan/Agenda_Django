from django.shortcuts import render, HttpResponse,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def loginUser (request):
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def listaEventos (request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) #get(id=1) #all()
    # if usuario == '0':
    #     evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submitEvento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        dataEvento = request.POST.get('dataEvento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        local = request.POST.get('local')
        Evento.objects.create(titulo=titulo,dataEvento=dataEvento,descricao=descricao,usuario=usuario,local=local)
    return redirect('/')

def submitLogin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password= password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    return redirect('/')
