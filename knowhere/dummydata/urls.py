from django.urls import path

from . import views
from .views import DummyListView


urlpatterns = [
	# path('',DummyListView.as_view(), name='dummy_list'),
	path('', views.DummyList, name = 'dummy_list'),
	path('<int:dummy_id>',views.DummyDetail, name = 'detail_view'),
	path('form', views.trialform, name = 'form'),
	# path('', views.dummylist, name = 'dummy_list'),
	
	
	]
