from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all() #ORM query to select all objects in the projects table
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

"""In line 6 of the code block above, we define a dictionary context. The dictionary only has one entry projects to which we assign our Queryset containing all projects. The context dictionary is used to send information to our template. Every view function you create needs to have a context dictionary. In line 9, context is added as an argument to render(). Any entries in the context dictionary are available in the template, as long as the context argument is passed to render(). You’ll need to create a context dictionary and pass it to render in each view function you create."""

def project_detail(request, pk):
    project = Project.objects.get(pk=pk) #get id, primary key(pk) object of the project that is being viewed
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

"""In line 14, we perform another query. This query retrieves the project with primary key, pk, equal to that in the function argument. We then assign that project in our context dictionary, which we pass to render(). Again, there’s a template project_detail.html, which we have yet to create."""