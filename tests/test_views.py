from django.test import TestCase, RequestFactory
from restaurant.models import Menu


class MenuViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.menu = Menu.objects.create(title="Limonade", price=80, inventory=100)
        
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items, 200)