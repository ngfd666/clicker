from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ToDoList, Item, Progress
from. forms import CreateNewList 	
# Create your views here.

def clicker(response):
	return render(response, "main/clicker.html", {})

def index(response, id):
	ls = ToDoList.objects.get(id=id)
	return render(response, "main/view.html", {"ls":ls})

def home(response):
	return render(response, "main/home.html", {})

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()

		
		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()

	return render(response, "main/create.html", {"form":form})

def save_progress(request):

    return JsonResponse({"yolo":"item"})

def get_progress(request):


    return JsonResponse({"yol123123o":"item"})

