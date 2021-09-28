from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # model to interact with by the form
        fields = ('username', 'email', 'password1', 'password2')  # fields in the form

    def __init__(self, *args, **kwargs):
        """Update widget attributes to use custom css in rendered form fields"""
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Your Username',
                                                    'maxlength': '150', 'autocomplete': 'none'})
        self.fields['email'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Your Email',
                                                  'autocomplete': 'none'})
        self.fields['password1'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Your Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Repeat Password'})


class UserLogInForm(AuthenticationForm):

    class Meta:
        model = User  # model to interact with by the form
        fields = ('username', 'password')  # fields in the form

    def __init__(self, *args, **kwargs):
        """Update widget attributes to use custom css in rendered form fields"""
        super(UserLogInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Your Username',
                                                     'maxlength': '150'})
        self.fields['password'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Your Password'})
