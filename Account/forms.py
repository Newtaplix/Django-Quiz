from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    email = forms.CharField(max_length=60, widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))
    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))



    class Meta:
        model = Account
        fields = ("email", "username","password1", "password2")

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=60, widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))

    class Meta:
        model = Account
        fields = ('email', 'password')
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("invalid login")

