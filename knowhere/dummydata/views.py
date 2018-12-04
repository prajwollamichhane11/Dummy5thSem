from django.shortcuts import render
from django.views.generic import(
	CreateView, ListView, DetailView, DeleteView, UpdateView)
from django.http import HttpResponse
from .forms import DummyModelForm

from .models import Dummy
# Create your views here.

class DummyListView(ListView):
	template_name = 'dummydata/dummy_list.html'
	context_object_name = 'dummy_data_list'
	queryset = Dummy.objects.all()
	
	'''the queryset in the ListView passes in the form of list so its name becomes dummy_list
	because of the <model name>_list. if we want to override it to be any name as in the 
	context we passed in function base view we can use context_object_name. '''

def trialform(request):
	form = DummyModelForm()
	context= {
	'form' : form
	}
	return render(request, 'dummydata/form.html', context)


