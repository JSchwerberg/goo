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

class PasswordResetRequestForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username or Email")

class PasswordResetForm(forms.Form):
    password = forms.CharField(max_length=64, widget=widgets.PasswordInput)
    confirm_password = forms.CharField(max_length=64, widget=widgets.PasswordInput)
    token = forms.CharField(max_length=20, widget=widgets.HiddenInput)
