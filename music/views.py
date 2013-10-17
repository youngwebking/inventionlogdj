from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import simplejson
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib import messages
from employee.models import Employee, Manager, ProductionManager, Draftsman, MachineTechnician, ModelBuilder
from music.models import Song, Playlist
from music.forms import SongForm
from django import template


# MUSIC PLAYER------------------------------------------------------------------------
def musicPlayer(request):
	user = request.user
	username = user.username
	if request.user.is_authenticated():
		try:
			song = request.GET['song']
			song = Song.objects.get(slug=song)
		except:
			song = ''
		try:
			playlist = request.GET['playlist']
			playlist = Playlist.objects.get(slug=playlist)
		except:
			playlist = ''
		employees = Employee.objects.all()
		try:
			employee = employees.get(username=username)
		except:
			employee = User.objects.get(username='admin')
		songs = Song.objects.all()
		playlists = Playlist.objects.filter(employee=employee)
		context = {'employee':employee, 'songs':songs, 'playlists':playlists}
		if playlist != '':
			playlists = Playlist.objects.filter(employee=employee)
			playlist = playlists.get(name=playlist)
			songs = Song.objects.filter(playlist=playlist)
			context = {'employee':employee, 'songs':songs, 'playlists':playlists, 'playlist':playlist}
		elif song != '':
			context = {'employee':employee, 'songs':songs, 'playlists':playlists, 'song':song}
		return render_to_response('musicplayer.html', context, context_instance=RequestContext(request))
	return HttpResponseRedirect('/')
	
# UPLOAD SONG------------------------------------------------------------
def UploadSong(request):
	user = request.user
	username = user.username
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = SongForm(request.POST, request.FILES)
			if form.is_valid():
				name = form.cleaned_data['name']
				artist = form.cleaned_data['artist']
				art = form.cleaned_data['art']
				song = request.FILES['song']
				newSong = Song(name=name,slug=slugify(name),artist=artist,art=art,song=song)
				newSong.save()
				return HttpResponseRedirect('/music-player/?song=' + name)
				
			context = {'form':form}
			return render_to_response('uploadsong.html', context, context_instance=RequestContext(request))
		form = SongForm()
		context = {'form':form}
		return render_to_response('uploadsong.html', context, context_instance=RequestContext(request))
	return HttpResponseRedirect('/')
	
# SINGLE SONG---------------------------------------------------------------
def song(request):
	if request.user.is_authenticated:
		results = {'success':False}
		GET = request.GET
		if GET.has_key('song'):
			slug = GET['song']
			song = Song.objects.get(slug=slug)
			context = {'song':song}
			results = {'success':True}
		json = simplejson.dumps(results)
		#return HttpResponse(json, mimetype='application/json')
		return HttpResponse(context)
	HttpResponseRedirect('/')
# SINGLE PLAYLIST
def playlist(request):
	if cuser.is_authenticated:
		results = {'success':False}
		GET = request.GET
		if GET.has_key('playlist'):
			slug = GET['playlist']
			song = Song.objects.get(slug=slug)
			results = {'success':True}
		json = simplejson.dumps(results)
		return HttpResponse(json, mimetype='application/json')
	HttpResponseRedirect('/')
