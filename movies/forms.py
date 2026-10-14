from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'category',
            'genre',
            'release_year',
            'rating',
            'duration',
            'poster_url',
            'backdrop_url',
            'video_url',
            'is_featured',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie or series title',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write a short synopsis or storyline...',
                'required': True,
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'genre': forms.Select(attrs={
                'class': 'form-select',
            }),
            'release_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1900,
                'max': 2099,
                'placeholder': 'e.g. 2024',
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
                'min': 0,
                'max': 10,
                'placeholder': 'e.g. 8.5',
            }),
            'duration': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 2h 15m or 3 Seasons',
            }),
            'poster_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/poster.jpg',
            }),
            'backdrop_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/backdrop.jpg (optional)',
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.youtube.com/embed/... (optional trailer URL)',
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create a password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username', 'autofocus': True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )
