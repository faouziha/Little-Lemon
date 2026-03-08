from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(Title='Pizza', Price=10.99, Inventory=5)
        self.item2 = Menu.objects.create(Title='Burger', Price=8.50, Inventory=10)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/') 
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)