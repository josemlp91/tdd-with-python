from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import *
from lists.models import *


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        """La ruta raiz tiene una vista asociada."""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """La pagina principal renderiza un contenido HTML válido."""
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string("home.html")
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        """El formulario principal lee datos del usuario."""
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())


    def test_home_page_can_save_a_POST_request_and_render(self):
        """El formulario principal lee datos del usuario y los representa en la vista HTML"""
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        
        expected_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
        self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        """ El sistema almacena correctamente objetos del todo"""
        first_item = Item()
        first_item.text = 'La primera cosa de la lista'
        first_item.save()

        second_item = Item()
        second_item.text = 'La segunda cosa'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.text, first_item.text )