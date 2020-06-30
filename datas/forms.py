from django import forms
from .models import Data
import os

class DataForm(forms.ModelForm):
    
    class Meta:
        model   =   Data
        fields  =   ('title', 'description', 'txt') 


        