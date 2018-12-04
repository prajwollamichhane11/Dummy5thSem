from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			'''if the form is valid we get the username from form'''
			username = form.cleaned_data.get('username')
			'''now sending the message for sucessful user creation'''
			messages.success(request, f'form created for user {username}!')
			'''now redirecting the user to login page'''
			return redirect ('log_in')
			
			
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})

def trial(request):
	return render (request, 'users/redirect.html')

@login_required
def profile(request):
	return render(request, 'users/profile.html')