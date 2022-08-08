import pytest
from django.test import TestCase
from tutorial.models import Tutorial
from django.urls import reverse
from .conftest import ConfTest

class RouteTest(TestCase):
    
    @pytest.mark.django_db
    def test_tutorial_home(self):
        tutorial_home_url = reverse("tutorial")
        
        response = self.client.get(tutorial_home_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/tutorial/"