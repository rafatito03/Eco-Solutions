from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo, {username}!')
                return redirect('home')  
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'login.html') 


def user_logout(request):
    auth_logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('home') 


def home(request):
    return render(request, 'home.html') 


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já está em uso.')
            return render(request, 'cadastro.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        auth_login(request, user)
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('home')

    return render(request, 'cadastro.html')

from .models import Local
from .models import Residuos

def mapa(request):
    locais = Local.objects.all()
    residuos = Residuos.objects.all()
    return render(request, 'mapa.html', {'locais': locais})

