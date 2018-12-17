from django.shortcuts import render
from django.views.generic import(
	CreateView, ListView, DetailView, DeleteView, UpdateView)
from django.http import HttpResponse
from .forms import DummyModelForm
from django.contrib.auth.decorators import login_required

from .models import Dummy
# Create your views here.

#this is class based view
class DummyListView(ListView):
	template_name = 'dummydata/dummy_list.html'
	context_object_name = 'dummy_data_list'
	queryset = Dummy.objects.all()
	
	'''the queryset in the ListView passes in the form of list so its name becomes dummy_list
	because of the <model name>_list. if we want to override it to be any name as in the 
	context we passed in function base view we can use context_object_name. '''

#this is function based view
def DummyList(request):
	context = {
		'dummy_data_list' : Dummy.objects.all()
	}
	return render(request, 'dummydata/dummy_list.html', context)

def DummyDetail(request, dummy_id):
	# return HttpResponse (f"you are looking at {dummy_id}")
	dummy_data_detail = Dummy.objects.get(pk = dummy_id)
	context = {
	'dummy_data_detail' : dummy_data_detail
	}
	return render (request, 'dummydata/dummy_detail.html', context)

@login_required
def trialform(request):
	form = DummyModelForm()
	context= {
	'form' : form
	}
	return render(request, 'dummydata/form.html', context)


