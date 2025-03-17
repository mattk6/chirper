from django import forms
from .models import Chirp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating a new user

    Attributes:
        Meta: Metadata for the form.
        password2: Field for confirming the password
    """
    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Username',
            'email': 'Email',
        }

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        """
        Validates if the two passwords match

        Returns:
            str: The cleaned password2 data

        Raises:
            forms.ValidationError: if the passwords do not match
        """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """
        Save the new user instance.

        Args:
            commit (bool): Whether to commit the save immediately

        Returns:
            User: The saved user instance.
        """
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class ChirpForm(forms.ModelForm):
    """
    Form for creating a new chirp

    Attributes:
        Meta: Metadata for the form
    """
    class Meta:
        model = Chirp
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': "What's on your mind?", 'rows': 3, 'cols': 30}),
        }

class ReplyForm(forms.ModelForm):
    """
    Form for creating a reply to a chirp

    Attributes:
        Meta: Metadata for the form
    """
    class Meta:
        model = Chirp
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': "Write a reply.", 'rows': 3, 'cols': 30}),
        }
