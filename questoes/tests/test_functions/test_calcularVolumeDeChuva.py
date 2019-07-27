from unittest import TestCase
from questoes.views.funcoes.calcularVolumeDeChuva import calcularVolumeDeChuva

class TestCalcularVolumeDeChuva(TestCase):
    def test_basic_case(self):
        minhaLista = [3, 2, 1, 2, 3]
        retorno = calcularVolumeDeChuva(minhaLista)
        resposta = 4
        self.assertEqual(retorno, resposta)

    def test_descending_numbers(self):
        minhaLista = [5, 4, 3, 2, 1]
        retorno = calcularVolumeDeChuva(minhaLista)
        resposta = 0
        self.assertEqual(retorno, resposta)

    def test_ascending_numbers(self):
        minhaLista = [1, 2, 3, 4, 5]
        retorno = calcularVolumeDeChuva(minhaLista)
        resposta = 0
        self.assertEqual(retorno, resposta)

    def test_same_value_repeated(self):
        minhaLista = [5, 5, 5, 5, 5, 5, 5]
        retorno = calcularVolumeDeChuva(minhaLista)
        resposta = 0
        self.assertEqual(retorno, resposta)

    def test_alternating_values(self):
        minhaLista = [5, 0, 5, 0, 5, 0, 5]
        retorno = calcularVolumeDeChuva(minhaLista)
        resposta = 15
        self.assertEqual(retorno, resposta)

    def test_negative_values(self):
        minhaLista = [5, -3, 2, 1, 0, 4, 7]
        retorno = calcularVolumeDeChuva(minhaLista)
        resposta = 21
        self.assertEqual(retorno, resposta)