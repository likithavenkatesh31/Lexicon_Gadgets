from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password')



