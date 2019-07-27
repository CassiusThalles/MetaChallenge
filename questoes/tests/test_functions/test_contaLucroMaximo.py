from unittest import TestCase
from questoes.views.funcoes.contaLucroMaximo import contaLucroMaximo

class TestContaLucroMaximo(TestCase):
    def test_basic_case(self):
        input = [1, 2, 3]
        resposta = 6
        retorno = contaLucroMaximo(input, 0, 0)
        self.assertEqual(retorno, resposta)

    def test_case_with_descending_numbers(self):
        input = [3, 2, 1]
        resposta = 6
        retorno = contaLucroMaximo(input, 0, 0)
        self.assertEqual(retorno, resposta)

    def test_alternating_values(self):
        input = [15, 0, 15, 0, 15, 0]
        resposta = 45
        retorno = contaLucroMaximo(input, 0, 0)
        self.assertEqual(retorno, resposta)

    def test_negative_and_positive_numbers(self):
        input = [0, 15, -3, 10, 15, 5, 8, -1]
        resposta = 50
        retorno = contaLucroMaximo(input, 0, 0)
        self.assertEqual(retorno, resposta)