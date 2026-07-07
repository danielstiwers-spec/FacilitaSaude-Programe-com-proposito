from django import forms
from apps.accounts.models import Usuario


class UsuarioForm(forms.Form):
    cpf = forms.CharField(
        required=True,
        label='CPF',
        widget=forms.TextInput(attrs={'placeholder': '000.000.000-00', 'maxlength': '14'}),
        error_messages={'required': 'Insira um CPF válido.'},
    )
    rg = forms.CharField(
        required=True,
        label='RG',
        widget=forms.TextInput(attrs={'placeholder': '00.000.000-0', 'maxlength': '12'}),
        error_messages={'required': 'Insira um RG válido.'},
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'nome@exemplo.com'}),
        error_messages={
            'required': 'Insira um e-mail válido.',
            'invalid': 'Insira um e-mail válido.',
        },
    )
    senha = forms.CharField(
        widget=forms.PasswordInput,
        label='Senha',
        error_messages={'required': 'Insira uma senha válida.'},
    )

    def save(self):
        username = self.cleaned_data['email'].split('@')[0]
        return Usuario.objects.create_user(
            username=username,
            email=self.cleaned_data['email'],
            password=self.cleaned_data['senha'],
            cpf=self.cleaned_data['cpf'],
        )
