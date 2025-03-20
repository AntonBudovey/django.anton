from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_text", "rating")


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput())
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class ChangeUserProfile(forms.ModelForm):
    class Meta:
        model = avatarka
        fields = ("pict",)
        widgets = {
            "pict": forms.FileInput(attrs={"class": "file_input", "label": "Select photo"})
        }


