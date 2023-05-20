from django import forms
from .models import BlogPost, Messages


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title here'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter content here'}),
        }

class MessagesPostForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter title here'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter email here'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter message here'}),
        }


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