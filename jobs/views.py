from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import Job

def find_jobs(request):
    if request.method == "GET":
        preco_minimo = request.GET.get('preco_minimo')
        preco_maximo = request.GET.get('preco_maximo')
        prazo_minimo = request.GET.get('prazo_minimo')
        prazo_maximo = request.GET.get('prazo_maximo')
        categoria = request.GET.get('categoria')
    if preco_minimo or preco_maximo or prazo_minimo or prazo_maximo or categoria:
        if not preco_minimo:
            preco_minimo = 0

        if not preco_maximo:
            preco_maximo = 999999

        if not prazo_minimo:
            prazo_minimo = datetime(year=1900, month=1, day=1)

        if not prazo_maximo:
            prazo_maximo = datetime(year=3000, month=1, day=1)

        if categoria == "D":
            categoria = ['D',]
        
        elif categoria == "VE":
            categoria = ['VE',]

        jobs = Job.objects.filter(price__gte=preco_minimo)\
            .filter(price__lte=preco_maximo)\
            .filter(deadline__gte=prazo_minimo)\
            .filter(deadline__lte=prazo_maximo)\
            .filter(category__in=categoria)\
            .filter(reserved=False)
    else:
        jobs = Job.objects.filter(reserved=False)
    return render(request, 'find_jobs.html', {'jobs': jobs})
