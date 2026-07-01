from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from python_modules.charts import build_chart_configs
from python_modules.consultas import checar_consultas_vazias, get_consultas_exemplo
from python_modules.rotina import inicializar_rotina
from .forms import UsuarioForm
from .models import Usuario, GlossaryEntry
from .initial_glossary_data import INITIAL_GLOSSARY_TERMS


def home_view(request):
    return index_view(request)


def index_view(request):
    chart_configs = build_chart_configs()
    consultas = get_consultas_exemplo()
    consultas_status = checar_consultas_vazias(consultas)

    return render(request, 'index.html', {
        'chart_configs': chart_configs,
        'consultas': consultas,
        'consultas_status': consultas_status,
    })


def routine_view(request):
    rotina_state = inicializar_rotina()
    return render(request, 'routine.html', {
        'rotina_state': rotina_state,
    })


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


def profile_view(request):
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

    return render(request, 'profile.html', {
        'usuario': usuario,
        'display_name': display_name,
        'initials': initials,
    })


def logout_view(request):
    request.session.flush()
    return redirect('/login/')


def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            usuario = Usuario.objects.filter(email=email).first()

            if usuario:
                if check_password(senha, usuario.senha):
                    request.session['usuario_id'] = usuario.id
                    return redirect('/user-cadastrado.html')
                else:
                    form.add_error('senha', 'Senha incorreta para este usuário.')
            else:
                usuario = form.save(commit=False)
                usuario.senha = make_password(senha)
                usuario.save()
                request.session['usuario_id'] = usuario.id
                return redirect('/user-cadastrado.html')
    else:
        form = UsuarioForm()

    return render(request, 'login.html', {'form': form})


def glossary_view(request):
    if not GlossaryEntry.objects.exists():
        for term_data in INITIAL_GLOSSARY_TERMS:
            GlossaryEntry.objects.create(**term_data)

    query = request.GET.get('q', '').strip()
    glossary_entries = GlossaryEntry.objects.all()

    if query:
        glossary_entries = glossary_entries.filter(title__icontains=query)
        glossary_entries |= GlossaryEntry.objects.filter(description__icontains=query)
        glossary_entries |= GlossaryEntry.objects.filter(symptoms__icontains=query)

    return render(request, 'glossary.html', {
        'glossary_entries': glossary_entries,
        'query': query,
    })
