from django.shortcuts import render,redirect
from .forms import PersonForm
from firstapp import models,forms
import json
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
	if request.method == 'POST':
		form=PersonForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
	form=PersonForm()
	alluser=models.Person.objects.all()
	return render(request,"home.html",{"form":form,"alluser":alluser})

def remove(request,username):
	models.Person.objects.get(firstname=username).delete()
	return redirect("home")

def Edit(request,username):
	username=models.Person.objects.get(firstname=username)
	form=PersonForm(instance=username)
	if request.method=="PUT":
		form = PersonForm(request.POST,instance=username)
		if form.is_valid():
			form.save()
			return redirect("home")
	return render(request,"editprofile.html",{"form":form})

def userinfo(request,username):
	info=serializers.serialize("json",[models.Person.objects.get(firstname=username)])
	return HttpResponse(info,content_type='json')
