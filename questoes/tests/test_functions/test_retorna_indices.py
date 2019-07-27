from unittest import TestCase
from questoes.views.funcoes.retornaIndices import retornaIndices

class TestRetornaIndices(TestCase):
    def test_basic_case(self):
        lista = [1, 2, 3, 4, 5, 6]
        alvo = 7
        resposta = [0, 5]
        retorno_da_funcao = retornaIndices(lista, alvo)
        self.assertEqual(retorno_da_funcao, resposta)

    def test_case_with_impossible_target(self):
        lista = [0, 0, 0, 0, 0, ]
        alvo = 7
        resposta = [0, 0]
        retorno_da_funcao = retornaIndices(lista, alvo)
        self.assertEqual(retorno_da_funcao, resposta)

    def test_case_with_negative_numbers_with_positive_target(self):
        lista = [-20, 1, 10, -5, 35, 2]
        alvo = 15
        resposta = [0, 4]
        retorno_da_funcao = retornaIndices(lista, alvo)
        self.assertEqual(retorno_da_funcao, resposta)

    def test_case_with_negative_numbers_with_negative_target(self):
        lista = [-20, 1, 10, -5, 35, 2]
        alvo = -25
        resposta = [0, 3]
        retorno_da_funcao = retornaIndices(lista, alvo)
        self.assertEqual(retorno_da_funcao, resposta)

    def test_case_list_with_one_number_repeated(self):
        lista = [2, 2, 2, 2, 2, 2, 2]
        alvo = 4
        resposta = [0, 6]
        retorno_da_funcao = retornaIndices(lista, alvo)
        self.assertEqual(retorno_da_funcao, resposta)

    def test_case_with_huge_integers(self):
        lista = [2147483647, 2147483647, 2147483647, 2147483647, 2147483647, 2147483647]
        alvo = 4294967294
        resposta = [0, 5]
        retorno_da_funcao = retornaIndices(lista, alvo)
        self.assertEqual(retorno_da_funcao, resposta)