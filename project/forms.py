from django import forms
from django.forms import ModelForm
from project.models import Project, Comment
	
class UploadDraftForm(forms.Form):

	stl = forms.FileField(required=False)
	dxf = forms.FileField(required=False)
	
class UploadModelForm(forms.Form):

	topView = forms.ImageField(required=False)
	View34 = forms.ImageField(required=False)
	leftView = forms.ImageField(required=False)
	frontView = forms.ImageField(required=False)
	rightView = forms.ImageField(required=False)
	
class ProjectSearchForm(forms.Form):
	
	CATEGORY_CHOICES = (
		('A', 'All'),
		('P', 'Pending'),
		('I', 'In Progress'),
		('C', 'Complete'),
	)
	
	searchbox = forms.CharField(max_length=100,required=False)
	category = forms.ChoiceField(choices=CATEGORY_CHOICES)
	
class CommentForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea)
