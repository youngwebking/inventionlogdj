from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

def index(request):
	context = None
	return render_to_response('index.html', context, context_instance=RequestContext(request))

def employeesAll(request):
	context = None
	return render_to_response('employeesall.html', context, context_instance=RequestContext(request))

def terms(request):
	context = None
	return render_to_response('terms.html', context, context_instance=RequestContext(request))

def help(request):
	context = None
	return render_to_response('help.html', context, context_instance=RequestContext(request))
