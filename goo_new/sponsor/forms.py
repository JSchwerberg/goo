from django import forms

class AuthKeyForm(forms.Form):
	token = forms.CharField(label="Authentication Token", max_length=12)
	