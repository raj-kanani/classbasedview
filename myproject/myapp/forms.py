from django import forms
from .models import Todos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class userform(forms.Form):
    name = forms.CharField(max_length=50)


class registerform(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'email']
        labels = {'email': 'Email'}

class todoform(forms.ModelForm):
    class Meta:
        model = Todos
        fields = '__all__'
