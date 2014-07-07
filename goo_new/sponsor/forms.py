from django import forms
from django.forms import widgets

class AuthKeyForm(forms.Form):
	token = forms.CharField(label="Authentication Token", max_length=12)
	
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=widgets.PasswordInput)
