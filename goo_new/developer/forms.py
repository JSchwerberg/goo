from django.forms import ModelForm
from .models import Developer

class DeveloperForm(ModelForm):
    class Meta:
        model = Developer

