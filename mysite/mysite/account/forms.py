from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('fullName', 'email', 'password', 'phoneNumber')

        widgets = {
            'fullName': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'email': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'password': forms.PasswordInput(attrs={'class':'form-control form-control-lg'}),
            'phoneNumber': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
        }