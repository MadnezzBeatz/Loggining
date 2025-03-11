from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Логин',}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class':'form-control',
                'placeholder':'Пароль'}))

class RegisterForm(UserCreationForm):
    # class Meta:
    #     model = User
    #     fields = ['username','email']
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Логин',}))
    email = forms.CharField(max_length=65, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Эл. почта', }))
    password1 = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Пароль', }))
    password2 = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'Повторите Пароль', }))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


        # widgets = {
        #     "username": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Логин',
        #     }),
        #     "email": forms.EmailInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Электронная почта',
        #     }),
            # "password1": forms.PasswordInput(attrs={
            #     'class': "form-control",
            #     'id': "inputPassword",
            #     'type': 'password',
            #     'placeholder': 'Пароль'
            # }),
            # "password2": forms.PasswordInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Ключ',
            # }),
        # }