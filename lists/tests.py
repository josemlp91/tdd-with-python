from django.test import TestCase
from django.urls import resolve
from lists.views import *

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_yrl_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
