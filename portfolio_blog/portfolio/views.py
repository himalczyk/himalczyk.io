from urllib import response
from django.shortcuts import render
from . models import Project


def homepage(response):
    return render(response, "portfolio/home.html", {})

def portfolio(request):
    projects = Project.objects.all()
    project = {
        "projects" : projects
    }
    return render(request, "portfolio/portfolio.html", project)
    
def about(response):
    return render(response, "portfolio/about.html", {})