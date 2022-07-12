from django.shortcuts import render
from .models import Tutorial

# Create your views here.
# def tutorial(request):
#     return render(request, "tutorial/tutorial_home.html")

def tutorial(request):
    tutorials = Tutorial.objects.all()
    tutorial = {
        'tutorials': tutorials
    }
    return render(request, 'tutorial/tutorial_home.html', tutorial)

def tutorial_content(request, pk):
    tutorial = Tutorial.objects.get(pk=pk)
    tutorial = {
        'tutorial' : tutorial
    }
    return render(request, 'tutorial/tutorial_content.html', tutorial)