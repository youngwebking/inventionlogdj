from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from music.models import Song

class SongForm(ModelForm):
	art = forms.ImageField(required=False)
	class Meta:
		model = Song
		exclude = ('slug', 'art',)
