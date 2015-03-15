from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from .models import User

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password',
				widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation',
				widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email','avatar','ciudad','nombre','edad')

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 != password2:
			raise forms.ValidationError("Password incorrecto")
		return password2
	
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])

		if commit:
			user.save()
		return user

class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ("email","avatar","ciudad","nombre","edad","is_active","is_admin")

	def clean_password(self):
		return self.initial["password"]


class EmailAuthenticationForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	
	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)


	def clean(self):
		email = self.cleaned_data.get("email")
		password = self.cleaned_data.get("password")

		self.user_cache = authenticate(email=email, password=password)

		if self.user_cache is None:
			raise forms.ValidationError("Usuario incorrecto")
		
		elif not self.user_cache.is_active:
			raise forms.ValidationError("Usuario inactivo")

		return self.cleaned_data

	def get_user(self):
		return self.user_cache