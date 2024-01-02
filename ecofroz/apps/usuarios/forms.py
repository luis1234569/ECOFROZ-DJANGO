from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from .models import Autorizador, Cotizador, Generador, User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('autorizador', 'generador', 'soporte',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('autorizador', 'generador',)


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        username = forms.EmailField(
            widget=forms.TextInput(
                attrs={
                    'class': 'row',
                }
            )
        )

        password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'class': 'row'
                }
            )
        )

class AutorizadorForm(forms.ModelForm):
    class Meta:
        model = Autorizador
        fields = [
            'first_name',
            'last_name',
            'e_mail',
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'e_mail': 'E-mail',
        }

        widgets = {
            'first_name': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'departamento',
                }
            ),

            'last_name': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'area',
                }
            ),

            'e_mail': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipoactivo',
                }
            ),
        }

class CotizadorForm(forms.ModelForm):
    class Meta:
        model = Cotizador
        fields = [
            'first_name',
            'last_name',
            'e_mail',
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'e_mail': 'E-mail',
        }

        widgets = {
            'first_name': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'departamento',
                }
            ),

            'last_name': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'area',
                }
            ),

            'e_mail': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipoactivo',
                }
            ),
        }

class GeneradorForm(forms.ModelForm):
    class Meta:
        model = Generador
        fields = [
            'first_name',
            'last_name',
            'e_mail',
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'e_mail': 'E-mail',
        }

        widgets = {
            'first_name': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'departamento',
                }
            ),

            'last_name': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'area',
                }
            ),

            'e_mail': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipoactivo',
                }
            ),
        }

