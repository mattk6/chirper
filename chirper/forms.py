from django import forms
from .models import Chirp

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # Add 'email' if you want email signup
        labels = {
            'username': 'Username',
            'email': 'Email',
        }

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class ChirpForm(forms.ModelForm):
    class Meta:
        model = Chirp
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': "What's on your mind?", 'rows': 3, 'cols': 30}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Chirp
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': "Write a reply.", 'rows': 3, 'cols': 30}),
        }
