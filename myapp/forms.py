from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username')
    password = forms.EmailField(label='Password')
    password2 = forms.EmailField(label='Confirm Password')
    class Meta:
        model = User
        fields = ['username','password']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Username')
    password = forms.EmailField(label='Password')
    class Meta:
        model = User
        fields = ['username', 'password']
