from django import forms

__author__ = 'eren'


class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(render_value=False))

class RegistrationForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(render_value=False))
    slug=forms.CharField(label=(u'slug'))
