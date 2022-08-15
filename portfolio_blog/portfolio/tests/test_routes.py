import pytest
from django.test import TestCase
from django.urls import reverse


class RouteTest(TestCase):
        
    @pytest.mark.django_db
    def test_home_page(self):
        homepage_url = reverse("homepage")
        
        response = self.client.get(homepage_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/"
        
    @pytest.mark.django_db
    def test_portfolio_page(self):
        portfolio_page_url = reverse("portfolio")
        
        response = self.client.get(portfolio_page_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/portfolio/"
    
    @pytest.mark.django_db
    def test_tutorial_page(self):
        tutorial_page_url = reverse("tutorial")
        
        response = self.client.get(tutorial_page_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/tutorial/"
        
    @pytest.mark.django_db
    def test_api_page(self):
        api_page_url = reverse("api_home")
        
        response = self.client.get(api_page_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/api/"
        
    @pytest.mark.django_db
    def test_about_page(self):
        about_page_url = reverse("about")
        
        response = self.client.get(about_page_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/about/"
        
    