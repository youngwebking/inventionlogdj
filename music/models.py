from django.db import models

class Song(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)
	
	artist = models.CharField(max_length=50)
	art = models.ForeignKey("SongArt",blank=True,null=True)
	song = models.FileField(upload_to='musicplayer/songs')
	
	def __unicode__(self):
		return self.name
		
class Playlist(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)
	employee = models.ForeignKey("employee.Employee")
	
	songs = models.ManyToManyField("Song")
	art = models.ForeignKey("SongArt",blank=True,null=True)
	
	def __unicode__(self):
		return self.name
		
class SongArt(models.Model):
	pic = models.ImageField(upload_to='musicplayer/songart')
