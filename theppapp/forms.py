from.models import Cheat
from django import forms

class Todo(forms.ModelForm):
    class Meta:
        model=Cheat
        fields=['name','priority','date']
