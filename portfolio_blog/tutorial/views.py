from django.shortcuts import render

# Create your views here.
def tutorial(request):
    return render(request, "tutorial/tutorial_home.html")

def tutorial_detail(request, pk):
    tutorial = Tutorial.objects.get(pk=pk)
    context = {
        'tutorials': tutorial
    }
    return render(request, 'tutorial/tutorial_detail.html', context)