from django import forms

class UserForm(forms.Form):
    username = forms.EmailField(label="UserName", max_length=128)
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput)