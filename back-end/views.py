from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import UsuarioForm
import requests

def cadastro_usuario(request):
    # 1. Busca os estados da API do IBGE (seu script)
    url_ibge = "https://ibge.gov.br"
    try:
        lista_estados = requests.get(url_ibge).json()
        lista_estados = sorted(lista_estados, key=lambda k: k['nome'])
    except Exception:
        lista_estados = []

    # 2. Se o usuário clicou no botão "Avançar" (Envio dos dados)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, estados_choices=lista_estados)
        
        if form.is_valid():
            # Cria o objeto mas não salva ainda para podermos criptografar a senha
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data['senha'])
            usuario.save() # Salva no banco de dados SQLite

            estado_selecionado = form.cleaned_data['estado']
            return HttpResponse(f"Sucesso! Cadastrado e estado ({estado_selecionado}) registrado.")

    # 3. Se o usuário está apenas entrando na página (Carregamento inicial)
    else:
        form = UsuarioForm(estados_choices=lista_estados)

    return render(request, 'login.html', {'form': form})
