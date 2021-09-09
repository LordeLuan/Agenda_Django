from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def consulta(request,titulo_evento):
    Evento.objects.get(titulo=titulo_evento)
    return Evento.titulo

