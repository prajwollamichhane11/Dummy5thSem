from django import forms
from .models import Dummy

class DummyModelForm(forms.ModelForm):
	class Meta:
		model = Dummy
		fields = [ 'name', 'date']