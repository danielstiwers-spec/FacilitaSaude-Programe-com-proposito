from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput,
        label='Senha',
        error_messages={
            'required': 'Insira uma senha válida.',
        }
    )
    
    class Meta:
        model = Usuario
        fields = ['cpf', 'rg', 'email', 'senha']
        labels = {
            'cpf': 'CPF',
            'rg': 'RG',
            'email': 'Email',
            'senha': 'Senha'
        }
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00', 'maxlength': '14'}),
            'rg': forms.TextInput(attrs={'placeholder': '00.000.000-0', 'maxlength': '12'}),
            'email': forms.EmailInput(attrs={'placeholder': 'nome@exemplo.com'}),
        }
        error_messages = {
            'cpf': {
                'required': 'Insira um CPF válido.',
            },
            'rg': {
                'required': 'Insira um RG válido.',
            },
            'email': {
                'required': 'Insira um e-mail válido.',
                'invalid': 'Insira um e-mail válido.',
            },
        }
