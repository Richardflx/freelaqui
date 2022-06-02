from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Job
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

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

def accept_job(request, id):
    job = Job.objects.get(id=id)
    job.professional = request.user
    job.reserved = True
    job.save()
    
    return redirect('/jobs/find_jobs')


def profile(request):
    if request.method == 'GET':
        jobs = Job.objects.filter(professional=request.user)
        return render(request, 'profile.html', {'jobs': jobs})

    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')

        usuario = User.objects.filter(username=username).exclude(id=request.user.id)

        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Username already exists')
            return redirect('/jobs/profile')

        usuario = User.objects.filter(email=email).exclude(id=request.user.id)

        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Email is already in use')
            return redirect('/jobs/profile')

        
        request.user.username = username
        request.user.email = email
        request.user.first_name = primeiro_nome
        request.user.last_name = ultimo_nome
        request.user.save()
        messages.add_message(request, constants.SUCCESS, 'Changes made successfully')
        return redirect('/jobs/profile')

