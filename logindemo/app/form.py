from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('address','profile_pic')