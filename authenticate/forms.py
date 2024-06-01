from django import forms

class RegisterForms(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='Password Confirm', 
                                       widget=forms.PasswordInput())