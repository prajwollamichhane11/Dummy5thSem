from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns=[
	path('register', user_views.register, name='sign_up'),
	path('profile', user_views.profile, name='user_profile'),
	path('trial', user_views.trial, name = 'trial'),
	# """ the login view requires the template. so we can pass the template as argument"""
	path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name= 'log_in'),
	path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'log_out'),
]