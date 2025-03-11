from .models import Steam
from django.forms import ModelForm, TextInput, NumberInput


class SteamForm(ModelForm):
    class Meta:
        model = Steam
        fields = ['login', 'password', 'secret_key', 'status']

        widgets = {
            "login":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Логин',
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }),
            "secret_key": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ключ',
            }),
            "status": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус аккаунта',
            }),
        }