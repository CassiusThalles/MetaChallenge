from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ViewTestCaseQuestao01(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_if_passing_correct_params_api_returns_200_ok(self):
        self.question_data = {"lista": [1,2,3,4,5,6], "alvo": 9}
        self.response = self.client.post(
            reverse('questao01'),
            self.question_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_if_passing_wrong_params_names_api_returns_400_internal_server_error(self):
        self.question_data = {"array": [1,2,3,4,5,6], "target": 9}
        self.response = self.client.post(
            reverse('questao01'),
            self.question_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_passing_wrong_param_values_api_returns_400(self):
        self.question_data = {"lista": 7, "alvo": "Hello"}
        self.response = self.client.post(
            reverse('questao01'),
            self.question_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_get_method_returns_405(self):
        self.response = self.client.get(
            reverse('questao01'),
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)