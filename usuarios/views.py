from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from .models import  ONG, Residuos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .forms import ONGForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo, {username}!')

                # Obtém a ONG do usuário e redireciona para a página específica dela
                try:
                    ong = user.ong
                    return redirect('ong_detail', pk=ong.pk)
                except ONG.DoesNotExist:
                    # Caso o usuário não tenha uma ONG associada, redireciona para 'mapa'
                    return redirect('mapa')
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



def mapa(request):
    locais = ONG.objects.all()
    return render(request, 'mapa.html', {'locais': locais})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

class OngDetailView(LoginRequiredMixin, DetailView):
    model = ONG
    template_name = 'ong_detail.html'
    context_object_name = 'ong'

    def get_queryset(self):
        # Filtra para que apenas a ONG do usuário logado seja acessada
        return ONG.objects.filter(usuario=self.request.user)

def verificar_ong(request, pk):
    ong = get_object_or_404(ONG, pk=pk, usuario=request.user)
    return render(request, 'ong_detail.html', {'ong': ong})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ONGForm
from .models import ONG

def update_ong(request, ong_id):
    ong = get_object_or_404(ONG, id=ong_id)
    
    # Verifica se o usuário logado é o dono da ONG
    if ong.usuario != request.user:
        return HttpResponseForbidden("Você não tem permissão para editar esta ONG.")
    
    if request.method == 'POST':
        form = ONGForm(request.POST, instance=ong)
        if form.is_valid():
            form.save()
            messages.success(request, "Informações atualizadas com sucesso!")
            return redirect('ong_detail', pk=ong.id)
    else:
        form = ONGForm(instance=ong)
    
    return render(request, 'ong_detail.html', {'form': form, 'ong': ong})
