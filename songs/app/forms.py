from django import forms
from .models import *

class AudioForm(forms.ModelForm):
    
    class Meta:
        model = NewSong
        fields = "__all__"
