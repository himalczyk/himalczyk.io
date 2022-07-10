from django.shortcuts import render
from .models import Tutorial

# Create your views here.
def tutorial(request):
    return render(request, "tutorial/tutorial_home.html")

# def tutorial_detail(request, pk):
#     tutorials = Tutorial.objects.get(pk=pk)
#     tutorial = {
#         'tutorials': tutorials
#     }
#     return render(request, 'tutorial/tutorial_detail.html', tutorial)