from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('fullName', 'address', 'city', 'comment', 'attachment')
        
        widgets = {
            'fullName': forms.TextInput(attrs={'class':'textinput textInput form-control', 'id': 'id_full_name'}),
            'address': forms.TextInput(attrs={'class':'textinput textInput form-control', 'id': 'id_address'}),
            'city': forms.TextInput(attrs={'class':'textinput textInput form-control', 'id': 'id_city'}),
            'comment': forms.TextInput(attrs={'class':'textinput textInput form-control', 'id': 'id_comment'}),
            'attachment': forms.FileInput(attrs={'class':'textinput textInput form-control',  'id': 'id_file', 'maxlength': 1000})
        }