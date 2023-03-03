from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django.db import models  
from django.forms import fields  
from django import forms
from import_export import resources



from .models import Image,noisemap





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username','password1','password2']
        

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("title","image")



