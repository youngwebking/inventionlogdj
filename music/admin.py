from django.contrib import admin
from music.models import Song, Playlist

class SongAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'artist',)
	search_fields = ['name', 'artist']

class PlaylistAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'employee',)
	search_fields = ['name', 'employee', 'songs']
	
admin.site.register(Song, SongAdmin)
admin.site.register(Playlist, PlaylistAdmin)
