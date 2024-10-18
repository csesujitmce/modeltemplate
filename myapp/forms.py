from django import forms
from myapp import models

class MovieForms(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.MovieModel