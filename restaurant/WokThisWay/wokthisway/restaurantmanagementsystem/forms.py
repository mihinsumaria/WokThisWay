from django import forms
from .models import Customer

class RegisterForm(forms.ModelForm):
	name=forms.CharField(label="Name")
	password=forms.CharField(label="Password",widget=forms.PasswordInput)
	confirmpassword=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
	name.widget.attrs.update({'class' : 'form-control'})
	password.widget.attrs.update({'class' : 'form-control'})
	confirmpassword.widget.attrs.update({'class' : 'form-control'})
	class Meta:
		model = Customer
		fields = ('name','password')

class LoginForm(forms.ModelForm):
	name=forms.CharField(label="Name")
	password=forms.CharField(label="Password",widget=forms.PasswordInput)
	tableID=forms.IntegerField(label="Table ID",min_value=1,max_value=6)
	name.widget.attrs.update({'class' : 'form-control'})
	password.widget.attrs.update({'class' : 'form-control'})
	tableID.widget.attrs.update({'class' : 'form-control'})
	class Meta:
		model = Customer
		fields = ('name','password')
