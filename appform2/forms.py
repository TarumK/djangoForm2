from .models import User
from django import forms

class UserForm(forms.Form):
    f_lname = forms.CharField(label='Имя')

