from django import forms
from Guest.models import register,services

class UserForm(forms.ModelForm):
    class Meta:
        model = register
        field = ['uname','email','password','fname','lname','address','phone']
        
    