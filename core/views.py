from django.shortcuts import render, HttpResponse,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

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
    #if usuario == "admin":
    #  evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    idEvento = request.GET.get('id')
    dados = {}
    if idEvento:
        dados['evento'] = Evento.objects.get(id=idEvento)
    return render(request, 'evento.html',dados)

@login_required(login_url='/login/')
def submitEvento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        dataEvento = request.POST.get('dataEvento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        local = request.POST.get('local')
        idEvento = request.POST.get('idEvento')
        if idEvento:
            evento=Evento.objects.get(id=idEvento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.dataEvento = dataEvento
                evento.descricao = descricao
                evento.local = local
                evento.save()
           # Evento.objects.filter(id=idEvento).update(titulo=titulo,descricao=descricao,dataEvento=dataEvento,local=local)
        else:
            Evento.objects.create(titulo=titulo,dataEvento=dataEvento,descricao=descricao,usuario=usuario,local=local)
    return redirect('/')

def deleteEvento(request,idEvento):
    usuario = request.user
    evento = Evento.objects.get(id=idEvento)
    if usuario == evento.usuario:
        evento.delete()
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
