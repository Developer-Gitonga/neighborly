from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Business

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','username','email','neighborhood','bio']
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['image','name','email','neighborhood']
        
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)