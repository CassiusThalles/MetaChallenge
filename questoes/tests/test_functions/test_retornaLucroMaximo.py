from unittest import TestCase
from questoes.views.funcoes.retornaLucroMaximo import retornaValorMaximo

class TestRetornaLucroMaximo(TestCase):
    def test_basic_case(self):
        input = [1, 2, 3]
        resposta = 2
        retorno = retornaValorMaximo(input)
        self.assertEqual(retorno, resposta)

    def test_case_with_descending_numbers(self):
        input = [3, 2, 1]
        resposta = 0
        retorno = retornaValorMaximo(input)
        self.assertEqual(retorno, resposta)

    def test_alternating_values(self):
        input = [15, 0, 15, 0, 15, 0]
        resposta = 15
        retorno = retornaValorMaximo(input)
        self.assertEqual(retorno, resposta)

    def test_negative_and_positive_numbers(self):
        input = [0, 15, -3, 10, 15, 5, 8, -1]
        resposta = 18
        retorno = retornaValorMaximo(input)
        self.assertEqual(retorno, resposta)