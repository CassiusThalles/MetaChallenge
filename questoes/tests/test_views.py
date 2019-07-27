from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from questoes.views import primeiraQuestaoView, segundaQuestaoView, terceiraQuestaoView, quartaQuestaoView

class TestPrimeiraQuestaoView(APITestCase):
    def test_post_data(self):
        url = reverse('questao01')
        data = {"lista": [1,2,3,4,5,6,7,8,9,10,11], "alvo": 18}
        response = self.client.post(url, data, format='json')
        self.assertEqual(primeiraQuestaoView.objects.get().resposta, [6, 10])