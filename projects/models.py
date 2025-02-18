from django import forms
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProjectForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Título"
        self.fields['description'].label = "Descrição"

    def clean_title(self):
        data = self.cleaned_data['title']
        if len(data) < 3:
            raise forms.ValidationError("O título precisa ter mais de 3 caracteres.")
        return data
    
    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data) < 10:
            raise forms.ValidationError("A descrição precisa ter mais de 10 caracteres.")
        return data