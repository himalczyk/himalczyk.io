from django.shortcuts import render
from . models import Project

# Create your views here.
def homepage(response):
    return render(response, "portfolio/base.html", {})

def portfolio(request):
    projects = Project.objects.all()
    project = {
        "projects" : projects
    }
    return render(request, "portfolio/home.html", project)
    
    