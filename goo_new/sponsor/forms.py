from django import forms
from django.forms import widgets

class AuthKeyForm(forms.Form):
	token = forms.CharField(label="Authentication Token", max_length=12)
	
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=widgets.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=64, widget=widgets.PasswordInput)
    confirm_password = forms.CharField(max_length=64, widget = widgets.PasswordInput)
    auth_key = forms.CharField(max_length=12, widget=widgets.HiddenInput)
