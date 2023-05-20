from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_modified = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Messages(models.Model):
    name = models.CharField(max_length=100)
    date_modified = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.name

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user