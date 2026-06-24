from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    # Campo extra no formulário que não precisa estar fixo no modelo
    estado = forms.ChoiceField(
        choices=[], # Começa vazio, vamos preencher com a API do IBGE
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields = ['cpf', 'rg', 'email', 'senha']
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'placeholder': '00.000.000-0'}),
            'email': forms.EmailInput(attrs={'placeholder': 'nome@exemplo.com'}),
            'senha': forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        }

    # Inicializador para injetar a lista da API do IBGE direto no campo de seleção
    def __init__(self, *args, **kwargs):
        estados_choices = kwargs.pop('estados_choices', [])
        super().__init__(*args, **kwargs)
        if estados_choices:
            # Transforma a lista da API no formato que o Django aceita: [('SP', 'São Paulo'), ...]
            self.fields['estado'].choices = [('', 'Selecione...')] + [
                (e['sigla'], e['nome']) for e in estados_choices
            ]
