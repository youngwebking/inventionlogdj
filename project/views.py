from project import helpers
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.template import RequestContext
from django.template.defaultfilters import slugify
from project.models import Project, Stl, Dxf, Image
from project.forms import UploadDraftForm, UploadModelForm, ProjectSearchForm
from employee.helpers import get_random_employee, get_next_employee
import re

# UPLOAD DRAFT FILES------------------------------------------------------------------
def upload_draft(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.is_authenticated():
			if request.user.username == project.draftsman.username:
				if request.method == 'POST':
					form = UploadDraftForm(request.POST, request.FILES)
					if form.is_valid():
						newstl = Stl(stl=request.FILES['stl'])
						newstl.save()
						
						newdxf = Dxf(dxf=request.FILES['dxf'])
						newdxf.save()
					
						project = Project.objects.get(slug=projectslug)
						project.stl = newstl
						project.dxf = newdxf
						project.save()
						return HttpResponseRedirect('/projects/' + projectslug + '/')
					else:
						form = UploadDraftForm()
						context = {'form': form, 'project': project}
						return render_to_response('upload-draft.html', context, context_instance=RequestContext(request))
				else:
					form = UploadDraftForm()
					context = {'form': form, 'project': project}
					return render_to_response('upload-draft.html', context, context_instance=RequestContext(request))
		return HttpResponseRedirect('/')
# UPLOAD MODEL IMAGES----------------------------------------------------		
def upload_model(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.is_authenticated():
			if request.user.username == project.modelBuilder.username:
				if request.method == 'POST':
					form = UploadModelForm(request.POST, request.FILES)
					if form.is_valid():
						try:
							new34 = Image(image=request.FILES['View34'])
							new34.save()
						except:
							pass
					
						try:
							newleft = Image(image=request.FILES['leftView'])
							newleft.save()
						except:
							pass
					
						try:
							newfront = Image(image=request.FILES['frontView'])
							newfront.save()
						except:
							pass
					
						try:
							newright = Image(image=request.FILES['rightView'])
							newright.save()
						except:
							pass
					
						project = Project.objects.get(slug=projectslug)
						try:
							project.modelImgTop = newtop
						except:
							pass
						try:
							project.modelImg34 = new34
						except:
							pass
						try:
							project.modelImgLeft = newleft
						except:
							pass
						try:
							project.modelImgFront = newfront
						except:
							pass
						try:
							project.modelImgRight = newright
						except:
							pass
						project.save()
						return HttpResponseRedirect('/projects/' + projectslug + '/')
					else:
						form = UploadModelForm()
						context = {'form': form, 'project': project}
						return render_to_response('upload-model.html', context, context_instance=RequestContext(request))
				else:
					form = UploadModelForm()
					context = {'form': form, 'project': project}
					return render_to_response('upload-model.html', context, context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

# ACCEPT PROJECT---------------------------------------------------------------------------------------------
def AcceptProject(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.username == project.productionManager.username:
			d = get_next_employee('D')
			t = get_next_employee('T')
			b = get_next_employee('B')
			project.accept_project(d, t, b)
			return HttpResponseRedirect('/projects/' + projectslug + '/')
	return HttpResponseRedirect('/')

# APPROVE DRAFTS---------------------------------------------------------------------------------------------
def ApproveDraft(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if request.user.username == project.productionManager.username:
		project.approve_draft()
		return HttpResponseRedirect('/projects/' + projectslug + '/')
	else:
		return HttpResponseRedirect('/')
		
# REJECT DRAFTS---------------------------------------------------------------------------------------------
def RejectDraft(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.username == project.productionManager.username:
			project.approve_draft()
			return HttpResponseRedirect('/projects/' + projectslug + '/')
	return HttpResponseRedirect('/')

# APPROVE PROTOTYPE---------------------------------------------------------------------------------------------
def ApprovePrototype(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.username == project.productionManager.username:
			project.approve_prototype()
			return HttpResponseRedirect('/projects/' + projectslug + '/')
	return HttpResponseRedirect('/')
		
# REJECT PROTOTYPE---------------------------------------------------------------------------------------------
def RejectPrototype(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.username == project.productionManager.username:
			project.reject_prototype()
			return HttpResponseRedirect('/projects/' + projectslug + '/')
	else:
		return HttpResponseRedirect('/')

# APPROVE MODELS---------------------------------------------------------------------------------------------
def ApproveModel(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.username == project.productionManager.username:
			project.approve_model()
			return HttpResponseRedirect('/projects/' + projectslug + '/')
	return HttpResponseRedirect('/')
		
# REJECT MODEL---------------------------------------------------------------------------------------------
def RejectModel(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.username == project.productionManager.username:
			project.reject_model()
			return HttpResponseRedirect('/projects/' + projectslug + '/')
	else:
		return HttpResponseRedirect('/')
		
# APPROVE ENTIRE PROJECT---------------------------------------------------------------------------------------------
def FinalApprove(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	if not project.finalApproved:
		if request.user.username == project.productionManager.username:
			project.final_approve()
			return HttpResponseRedirect('/projects/' + projectslug + '/')
	return HttpResponseRedirect('/')
		
# PROJECTS-------------------------------------
def ProjectsAll(request):
	projects = Project.objects.all()
	if request.method == 'POST':
		form = ProjectSearchForm(request.POST)
		if form.is_valid():
			keywords = form.cleaned_data['searchbox']
			projects = projects.filter(name__icontains=keywords)
			if form.cleaned_data['category'] == 'P':
				projects = projects.filter(status='P')
			elif form.cleaned_data['category'] == 'I':
				projects = projects.filter(status='I')
			elif form.cleaned_data['category'] == 'C':
				projects = projects.filter(status='C')
			context = {'projects':projects, 'form':form, 'keywords':keywords}
			return render_to_response('projectsall.html', context, context_instance=RequestContext(request))
	else:
		form = ProjectSearchForm()
		context = {'projects':projects, 'form':form}
		return render_to_response('projectsall.html', context, context_instance=RequestContext(request))
	
def SpecificProject(request, projectslug):
	project = Project.objects.get(slug=projectslug)
	context = {'project': project}
	return render_to_response('singleproject.html', context, context_instance=RequestContext(request))
