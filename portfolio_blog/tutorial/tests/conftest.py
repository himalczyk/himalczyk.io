import pytest
import datetime
from django.utils.timezone import make_aware
from tutorial.models import Tutorial
from django.test import TestCase

naive_date_time = datetime.datetime.now()
date_time = make_aware(naive_date_time)

class ConfTest(TestCase):
    
    @pytest.mark.django_db
    def test_add_tutorial_post(self):
        test_tutorial = Tutorial(
            title="test_title",
            description="test_description",
            content = "test_content",
            pub_date = date_time
        )
        
        test_tutorial.save()
        assert Tutorial.objects.count() > 0
        return test_tutorial
    