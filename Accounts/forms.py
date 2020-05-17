from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .choices import VILLES
from django.core.exceptions import ValidationError
from .models import DeliveryPerson
from .random_code import CODE


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ville = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=VILLES)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'ville')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise ValidationError("Les Mots de Passe de correspondent pas")

        return cd['password2']


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))


class DeliveryPersonForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ville = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=VILLES)
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}), initial=CODE)

    class Meta:
        model = DeliveryPerson
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'ville', 'code')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise ValidationError("Les Mots de Passe de correspondent pas")

        return cd['password2']


class EmailResetForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
