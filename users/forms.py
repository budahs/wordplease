from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    usr = forms.CharField(label='Username')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Enter valid Username')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            return user