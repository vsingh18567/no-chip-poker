from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
import json


class GameViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_post_get_games(self):
        data = self.client.get(reverse("game-list")).data
        self.assertEqual(len(data), 0)
        a = self.client.post(
            reverse("game-create"),
            data=json.dumps({"starting_money": 1000}),
            content_type="application/json",
        )
        self.assertEqual(a.status_code, 200)
        data = json.loads(self.client.get(reverse("game-list")).content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["starting_money"], 1000)
        self.assertEqual(len(data[0]["name"]), 7)

    def test_bad_post_request(self):
        a = self.client.post(reverse("game-create"))
        self.assertEqual(a.status_code, 400)

    def test_patch(self):
        self.client.post(
            reverse("game-create"),
            data=json.dumps({"starting_money": 1000}),
            content_type="application/json",
        )
        id = json.loads(self.client.get(reverse("game-list")).content)[0]["id"]
        a = self.client.put(reverse("game-update", kwargs={"id": id}), data={
            "big_blind": 100
        })
        print(a.status_code)
