from django.db import models
from django import forms

class Student(models.Model):
    fullname = models.CharField(max_length=500)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

class StudentForm(forms.Form):
    fullname = forms.CharField(max_length=500)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

    def clean_fullname(self):
        data = self.cleaned_data['fullname']
        if len(data) < 3:
            raise forms.ValidationError("O nome precisa ter mais de 3 caracteres.")
        return data