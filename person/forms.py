from django import forms
from .models import Genral

class GenralForm(forms.ModelForm):
    class Meta:
        model = Genral
        fields =['id', 'name', 'url']



