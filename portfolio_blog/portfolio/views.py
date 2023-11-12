from datetime import datetime

from django.shortcuts import render

from .models import Project


def homepage(response):
    current_year = datetime.now().year
    return render(response, "portfolio/home.html", {"current_year": current_year})


def portfolio(request):
    projects = Project.objects.all()
    project = {"projects": projects}
    return render(request, "portfolio/portfolio.html", project)


def about(response):
    return render(response, "portfolio/about.html", {})
