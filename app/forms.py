from typing import Any
from django import forms

def validate_for_x(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('Invalid input')
    
def validate_for_len(data):
    if len(data)<4:
        raise forms.ValidationError('Input should be more than 4 character')




class SchoolForm(forms.Form):
    Sname = forms.CharField(validators=[validate_for_x])
    S_Principal = forms.CharField(validators=[validate_for_len])
    S_Loc = forms.CharField()
    Email = forms.EmailField()
    ReEnter_Email = forms.EmailField()
    
    def clean(self):
        e = self.cleaned_data['Email']
        re = self.cleaned_data['ReEnter_Email']
        
        if e != re:
            raise forms.ValidationError('Email mismatched')