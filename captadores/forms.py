from dataclasses import fields
from django import forms
from .models import Captador

class CaptadorForm(forms.ModelForm):
    class Meta:
        model = Captador
        fields = "__all__"
        # exclude = ('marca',)
