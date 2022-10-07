# from audioop import reverse
from uuid import RESERVED_MICROSOFT
from wsgiref.util import request_uri
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# tasks = [] #list

# tasks = ["coding","reviewing"]

class newTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    if "tasks" not in request.session:
        print("hello")
        # request.session["tasks"] = []
    return render(request, "tasks/index.html",{
        "tasks":  request.session["tasks"]   # tasks
    })


def add(request):
    # tasks = []
    # tasks = request.session["tasks"]
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # request.session["tasks"]
            request.session["tasks"] += [task] # task already stored
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "form": form
            })


    return render(request, "tasks/add.html",{
        "form" : newTaskForm()
    })
    