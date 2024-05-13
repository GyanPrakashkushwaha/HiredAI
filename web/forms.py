from django import forms
from .models import Resume

class ResumeForm(forms.Form):
    resume_field = forms.FileField()
    class Meta:
        model = Resume
        fields = ['resume_file']


class GeeksForm(forms.Form): 
    name = forms.CharField() 
    geeks_field = forms.FileField() 