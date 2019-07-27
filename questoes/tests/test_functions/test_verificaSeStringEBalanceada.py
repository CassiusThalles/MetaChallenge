from unittest import TestCase
from questoes.views.funcoes.verificaSeStringEBalanceada import balanceada

class TestVerificaSeStringEBalanceada(TestCase):
    def test_basic_case(self):
        sequencia = "{(([{}]))}"
        resposta = "SIM"
        retorno = balanceada(sequencia)
        self.assertEqual(retorno, resposta)

    def test_basic_case2(self):
        sequencia = "{(([{]}))}"
        resposta = "NÃO"
        retorno = balanceada(sequencia)
        self.assertEqual(retorno, resposta)

    def test_case_with_numbers(self):
        sequencia = "{(([{11}]))}"
        resposta = "SIM"
        retorno = balanceada(sequencia)
        self.assertEqual(retorno, resposta)