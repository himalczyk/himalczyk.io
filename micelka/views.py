from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Micelka."""
    return render(request,
        'micelka/index.html')