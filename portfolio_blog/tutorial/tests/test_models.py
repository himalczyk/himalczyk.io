import pytest
import datetime
from django.utils.timezone import make_aware
from django.test import TestCase
from .conftest import ConfTest


class ModelTest(TestCase):

    @pytest.mark.django_db
    def test_add_tutorial_post(self):
        new_tutorial = ConfTest.test_add_tutorial_post(self)
        
        assert new_tutorial.title == "test_title"
        assert new_tutorial.description == "test_description"
        assert new_tutorial.content == "test_content"