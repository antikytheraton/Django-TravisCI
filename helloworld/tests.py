from django.test import TestCase

# Create your tests here.
class FirstTest(TestCase):

    def setUp(self):
        self.a = 1
        self.b = 2

    def test_suma(self):
        self.assertEqual(self.a + self.b, 3)
