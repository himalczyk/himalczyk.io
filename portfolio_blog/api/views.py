from django.shortcuts import render

# Create your views here.
def api_home(response):
    return render(response, 'api/api_home.html')