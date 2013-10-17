from dajaxice.decorators import dajaxice_register
from django.core import Dajax

@dajaxice_register
def getSongBySlug(request, slug):
	dajax = Dajax()
	song = Song.objects.get(slug=slug)
	dajax.assign('#song-title','innerHTML',str(song.name))
	return dajax.json()
	
def assign_example(request):
    dajax = Dajax()
    dajax.assign('#button', 'value', 'Click here!')
    dajax.assign('div .alert', 'innerHTML', 'This email is invalid')
    return dajax.json()
