
from django import forms
from .models import Chirp

class ChirpForm(forms.ModelForm):
    class Meta:
        model = Chirp
        fields = ['content']