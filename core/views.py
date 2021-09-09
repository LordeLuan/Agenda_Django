from django.shortcuts import render, HttpResponse,redirect
from core.models import Evento

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def listaEventos (request):
    #usuario = request.user
    evento = Evento.objects.all() #filter(usuario=usuario)  #get(id=1)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)