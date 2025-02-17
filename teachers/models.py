from django.db import models
from django import forms

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class TeacherForm(forms.Form):
    name = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise forms.ValidationError("Por favor, insira um email válido.")
        if not email.endswith('.com'):
            raise forms.ValidationError("Por favor, insira um email válido.")
        return email

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Por favor, insira um nome válido.")
        return name
    
    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']
        if len(lastname) < 3:
            raise forms.ValidationError("Por favor, insira um sobrenome válido.")
        return lastname
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data.get('email')
    #     name = cleaned_data.get('name')
    #     lastname = cleaned_data.get('lastname')
    #     print(email)
    #     if email and not email.endswith('.com'):
    #         raise forms.ValidationError("Por favor, insira um email válido.")
    #     if len(name) < 3:
    #         raise forms.ValidationError("Por favor, insira um nome válido.")
    #     if len(lastname) < 3:
    #         raise forms.ValidationError("Por favor, insira um sobrenome válido.")
    #     if not email or not name or not lastname:
    #         raise forms.ValidationError("Por favor, preencha todos os campos.")