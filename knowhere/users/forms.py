from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	# middle_name = forms.CharField(max_length =30, null = True)
	gender_choice = (
		('m', 'Male'),
		('f', 'Female'),
		('n', 'No')
		)
	# gender = forms.CharField(max_length=1, choices= gender_choice)

	gender = forms.ChoiceField(
        
        choices=gender_choice,
    )

	class Meta:
		model = User
		fields = ['username', 'password1','password2', 'email', 'first_name', 'last_name', 'gender']
