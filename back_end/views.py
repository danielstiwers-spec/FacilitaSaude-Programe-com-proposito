from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import UsuarioForm

def login_view(request):
    form = UsuarioForm()
    return render(request, 'login.html', {'form': form})

def user_cadastrado_view(request):
    return render(request, 'user-cadastrado.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            # Cria o objeto mas não salva ainda para podermos criptografar a senha
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data['senha'])
            usuario.save()  # Salva no banco de dados

            # Redireciona para página de usuário cadastrado
            return redirect('/user-cadastrado/')

    else:
        form = UsuarioForm()

    return render(request, 'login.html', {'form': form})
