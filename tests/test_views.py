from django.test import TestCase
from restaurant.models import Menu
from django.core.serializers import serialize


class MenuViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.menu = Menu.objects.create(title="Limonade", price=80, inventory=100)
        
    def test_getall(self):
        items = serialize('json', Menu.objects.all())
        response = self.client.get('/restaurant/menu/items/')
        self.assertEqual(items, response)