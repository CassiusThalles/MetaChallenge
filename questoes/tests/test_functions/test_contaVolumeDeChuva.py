from unittest import TestCase
from questoes.views.funcoes.contaVolumeDeChuva import contaVolumeDeChuva

class TestContaVolumeDeChuva(TestCase):
    def test_basic_case(self):
        minhaLista = [3, 2, 1, 2, 3]
        maiorAltura = max(minhaLista)
        mapeamento = [0] * maiorAltura
        maiorAlturaAlcancada = 0
        volumeDeChuva = 0
        retorno = contaVolumeDeChuva(minhaLista, mapeamento, maiorAlturaAlcancada, volumeDeChuva)
        resposta = 4
        self.assertEqual(retorno, resposta)

    def test_descending_numbers(self):
        minhaLista = [5, 4, 3, 2, 1]
        maiorAltura = max(minhaLista)
        mapeamento = [0] * maiorAltura
        maiorAlturaAlcancada = 0
        volumeDeChuva = 0
        retorno = contaVolumeDeChuva(minhaLista, mapeamento, maiorAlturaAlcancada, volumeDeChuva)
        resposta = 0
        self.assertEqual(retorno, resposta)

    def test_ascending_numbers(self):
        minhaLista = [1, 2, 3, 4, 5]
        maiorAltura = max(minhaLista)
        mapeamento = [0] * maiorAltura
        maiorAlturaAlcancada = 0
        volumeDeChuva = 0
        retorno = contaVolumeDeChuva(minhaLista, mapeamento, maiorAlturaAlcancada, volumeDeChuva)
        resposta = 0
        self.assertEqual(retorno, resposta)

    def test_same_value_repeated(self):
        minhaLista = [5, 5, 5, 5, 5, 5, 5]
        maiorAltura = max(minhaLista)
        mapeamento = [0] * maiorAltura
        maiorAlturaAlcancada = 0
        volumeDeChuva = 0
        retorno = contaVolumeDeChuva(minhaLista, mapeamento, maiorAlturaAlcancada, volumeDeChuva)
        resposta = 0
        self.assertEqual(retorno, resposta)

    def test_alternating_values(self):
        minhaLista = [5, 0, 5, 0, 5, 0, 5]
        maiorAltura = max(minhaLista)
        mapeamento = [0] * maiorAltura
        maiorAlturaAlcancada = 0
        volumeDeChuva = 0
        retorno = contaVolumeDeChuva(minhaLista, mapeamento, maiorAlturaAlcancada, volumeDeChuva)
        resposta = 15
        self.assertEqual(retorno, resposta)

    def test_negative_values(self):
        minhaLista = [5, -3, 2, 1, 0, 4, 7]
        maiorAltura = max(minhaLista)
        mapeamento = [0] * maiorAltura
        maiorAlturaAlcancada = 0
        volumeDeChuva = 0
        retorno = contaVolumeDeChuva(minhaLista, mapeamento, maiorAlturaAlcancada, volumeDeChuva)
        resposta = 21
        self.assertEqual(retorno, resposta)