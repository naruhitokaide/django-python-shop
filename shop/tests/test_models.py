from django.test import TestCase
from shop.models import Brand

class AnimalTestCase(TestCase):
    def setUp(self):
        Brand.objects.create(name="lion", sound="roar")
        Brand.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Brand.objects.get(name="lion")
        cat = Brand.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')