from django.test import TestCase
from django.urls import reverse


class RouteTest(TestCase):
    
    def test_api_home_page(self):
        api_home_url = reverse("api_home")
        
        response = self.client.get(api_home_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/api/"
        
    def test_podcasts_page(self):
        podcasts_url = reverse("podcasts")
        
        response = self.client.get(podcasts_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/podcasts/"
        
    def test_videos_page(self):
        videos_url = reverse("yt_video_index")
        
        response = self.client.get(videos_url)
        
        assert response.status_code == 200
        assert response.context["request"].path == "/yt_channel_tutorials/"