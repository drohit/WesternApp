from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from Person.models import Person

class RegistrationForm(ModelForm):
	email = forms.CharField(label=(u'Email Address'), widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"E-Mail"}))
	#email = forms.EmailField(label=(u'Email Address'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False, attrs={"class":"form-control", "placeholder":"Password"}))
	#password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
	name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Full Name"}))

	class Meta:
		model = Person
		exclude = ('user',)

	def clean_email(self):
		''' Return email if a user with the desired email does not already exist. Otherwise,
		raise a ValidationError '''
		email = self.cleaned_data['email']
		try:
			User.objects.get(email = email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError("That email is already in use! Please select another.")


class LoginForm(forms.Form):
	email = forms.CharField(label=(u'Email Address'))
	password = forms.CharField(label=(u'Password'), widget = forms.PasswordInput(render_value=False))

class RecoveryForm(forms.Form):
	email = forms.CharField(label=(u'Email Address'))

class ProfileForm(forms.Form):
	email = forms.CharField(label=(u'Email Address'), required=False)
	name = forms.CharField(label=(u'Name'), required=False)
	password1 = forms.CharField(label=(u'Password'), widget = forms.PasswordInput(render_value=False), required=False)
	password2 = forms.CharField(label=(u'Password'), widget = forms.PasswordInput(render_value=False), required=False)

