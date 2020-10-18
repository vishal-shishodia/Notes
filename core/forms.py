from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','password1','password2']

class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['mobile','address']

class NoteForm(forms.ModelForm):
	
	class Meta:
		model=Note
		fields=['title','content']

class ImageForm(forms.ModelForm):
	image=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
	class Meta:
		model=Image
		fields=['image']