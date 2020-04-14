from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page #(2)
from django.template.loader import render_to_string

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolve_to_home_page_view(self):
        found=resolve('/') #(1)
        self.assertEqual(found.func,home_page)#(1)

    def test_home_page_returns_correct_html(self):
        response=self.client.get('/')#1
        self.assertTemplateUsed(response,'home.html')#3
        

