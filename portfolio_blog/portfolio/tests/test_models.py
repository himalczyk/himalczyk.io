import pytest
from django.test import TestCase
from portfolio.models import Project


class ModelTest(TestCase):

    @pytest.mark.django_db
    def test_add_portfolio_project(self):
        new_project = Project()
        new_project.title = "test_title"
        new_project.description = "test_description"
        
        old_project_obj_count = Project.objects.filter().count()
        new_project.save()
        new_project_obj_count = Project.objects.filter().count()
        
        assert new_project.title == "test_title"
        assert new_project.description == "test_description"
        assert old_project_obj_count < new_project_obj_count