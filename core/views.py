from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import *
from .forms import *

def index(request):
	return render(request,'core/index.html')

@login_required
def UserHome(request):
	profile=Profile.objects.get(user=request.user)
	notes=Note.objects.filter(profile=profile)
	context={'notes':notes}
	return render(request,'core/user_home.html',context)

def AdminHome(request):
	profiles=Profile.objects.all()
	return render(request,'core/admin_home.html',{'profiles':profiles})



def Register(request):
	if request.user.is_authenticated:
		return redirect('user_home')
	context={}
	form1=UserForm()
	form2=ProfileForm()
	if request.POST:
		form1=UserForm(request.POST)
		form2=ProfileForm(request.POST, request.FILES or None)
		if form1.is_valid() and form2.is_valid():
			user=form1.save(commit=False)
			user.save()
			profile=form2.save(commit=False)
			profile.user=user
			profile.save()
			login(request,user)
			return redirect('user_home')
		else:
			context={'form1':form1,'form2':form2}
	else:
		context={'form1':form1,'form2':form2}
	return render(request,'core/register.html',context)

def AddNote(request):
	title='Create'
	profile=Profile.objects.get(user=request.user)
	ImageFormSet=modelformset_factory(Image,form=ImageForm,extra=3)
	form1=NoteForm()
	form2=ImageFormSet(queryset=Image.objects.none())
	if request.POST:
		form1=NoteForm(request.POST)
		form2=ImageFormSet(request.POST, request.FILES,queryset=Image.objects.none())
		
		if form1.is_valid() and form2.is_valid():
			note=form1.save(commit=False)
			note.profile=profile
			note.save()
			for form in form2.cleaned_data:
				if form:
					image=form['image']
					photo=Image(note=note,image=image)
					photo.save()
			return redirect('user_home')
		else:
			context={'form1':form1,'form2':form2,'title':title}
	else:
		context={'form1':form1,'form2':form2,'title':title}
	return render(request,'core/addnote.html',context)

def DetailNote(request,pk):
	note=get_object_or_404(Note,pk=pk)
	return render(request,'core/detail.html',{'note':note})

def UpdateNote(request,pk):
	title='Update'
	note=Note.objects.get(id=pk)
	profile=Profile.objects.get(user=request.user)
	ImageFormSet=modelformset_factory(Image,form=ImageForm,extra=3)
	form1=NoteForm()
	form2=ImageFormSet(queryset=Image.objects.none())
	if request.POST:
		form1=NoteForm(request.POST,instance=note)
		form2=ImageFormSet(request.POST, request.FILES,queryset=Image.objects.none())
		
		if form1.is_valid() and form2.is_valid():
			note=form1.save(commit=False)
			note.profile=profile
			note.save()
			for form in form2.cleaned_data:
				if form:
					image=form['image']
					photo=Image(note=note,image=image)
					photo.save()
			return redirect('user_home')
		else:
			context={'form1':form1,'form2':form2,'title':title}
	else:
		context={'form1':form1,'form2':form2,'title':title}
	return render(request,'core/addnote.html',context)



def DeleteNote(request,pk):
	note = get_object_or_404(Note, id=pk)
	note.delete()
	return redirect("user_home")



def LoginSuccess(request):
	if request.user.is_superuser:
		return redirect("admin_home")

	else:
		return redirect("user_home")

def LogOut(request):
	logout(request)
	return redirect('index')


