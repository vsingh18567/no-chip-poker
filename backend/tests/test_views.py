from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
import json

class GameViewTestCase(TestCase):

	def setUp(self):
		self.client = APIClient()

	def test_get_nothing(self):
		data = self.client.get(reverse("game-list")).data
		self.assertEqual(len(data), 0)
		a = self.client.post(reverse("game-create"), data=json.dumps({
			"name": "637fdx",
		}), content_type = "application/json")
		print(a.status_code)
		data = self.client.get(reverse("game-list")).data
		self.assertEqual(len(data), 1)
