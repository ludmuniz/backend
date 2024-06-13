from django.shortcuts import render
from django.http import HttpResponse

def abre_index(request):
    mensagem = "Abrindo a Index do projeto"
    return HttpResponse(mensagem)