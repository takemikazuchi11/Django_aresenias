from django import forms
from Guest.models import register,services

class UForm(forms.ModelForm):
    class Meta:
        model = register
        fields = ['uname','email','password','fname','lname','address','phone']

class PForm(forms.ModelForm):
    class Meta:
        model = services
        fields = ['name','discount','price','details']
        
        
        
        
        