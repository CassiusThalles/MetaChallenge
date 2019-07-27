from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ViewTestCaseQuestao02(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_if_passing_correct_params_api_returns_200_ok(self):
        self.question_data = {"sequencia": "[{{/}}]"}
        self.response = self.client.post(
            reverse('questao02'),
            self.question_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_if_passing_wrong_params_names_api_returns_400_bad_request(self):
        self.question_data = {"array": "[]{}{}"}
        self.response = self.client.post(
            reverse('questao02'),
            self.question_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_passing_wrong_param_values_api_returns_400(self):
        self.question_data = {"sequencia": 7}
        self.response = self.client.post(
            reverse('questao02'),
            self.question_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_get_method_returns_405(self):
        self.response = self.client.get(
            reverse('questao02'),
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)