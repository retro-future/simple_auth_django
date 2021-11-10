from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from simple_auth.models import CustomAuthUser


class RegistrationForm(UserCreationForm):
    """
        Form for Registering new users
    """
    email = forms.CharField(max_length=150, help_text="Enter some username")

    class Meta:
        model = CustomAuthUser
        fields = ("email", "username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields
        """
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],
                      self.fields['username'],
                      self.fields['password1'],
                      self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})


class CustomAuthUserForm(forms.ModelForm):
    """
        Form for authorization users
    """
    class Meta:
        model = CustomAuthUser
        fields = ('email', 'password')
        widgets = {
            "email": forms.TextInput(
                attrs={'placeholder': 'Username', 'class': 'form-control', 'id': 'floatingInput'}),
            "password": forms.PasswordInput(
                attrs={'placeholder': 'Password', 'class': 'form-control', 'id': 'floatingInput'})
        }

    def __init__(self, *args, **kwargs):
        """
        specifying styles to fields
        """
        super(CustomAuthUserForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'], self.fields['password']):
            field.widget.attrs.update({"class": "form-control"})

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid Login')
