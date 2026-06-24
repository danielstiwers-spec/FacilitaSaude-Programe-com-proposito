from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import UsuarioForm
from .models import Usuario

def login_view(request):
    form = UsuarioForm()
    return render(request, 'login.html', {'form': form})

def user_cadastrado_view(request):
    usuario = None
    usuario_id = request.session.get('usuario_id')

    if usuario_id:
        try:
            usuario = Usuario.objects.get(pk=usuario_id)
        except Usuario.DoesNotExist:
            usuario = None

    if not usuario:
        return redirect('/login/')

    display_name = usuario.email.split('@')[0].replace('.', ' ').title()
    initials = ''.join([part[0] for part in display_name.split() if part]).upper()[:2]

    return render(request, 'user-cadastrado.html', {
        'usuario': usuario,
        'display_name': display_name,
        'initials': initials,
    })

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data['senha'])
            usuario.save()
            request.session['usuario_id'] = usuario.id
            return redirect('/user-cadastrado/')

    else:
        form = UsuarioForm()

    return render(request, 'login.html', {'form': form})
