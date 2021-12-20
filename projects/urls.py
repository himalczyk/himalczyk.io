from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"), # value passed in the URL is an integer, and its variable name is pk.
]

"""In line 5, we hook up the root URL of our app to the project_index view. It is slightly more complicated to hook up the project_detail view. To do this, we want the URL to be /1, or /2, and so on, depending on the pk of the project."""