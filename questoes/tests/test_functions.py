import unittest
from questoes.views.funcoes import calcularVolumeDeChuva, contaLucroMaximo,contaVolumeDeChuva, retornaIndices, retornaLucroMaximo,verificaSeStringEBalanceada

class TestRetornaIndices(unittest.TestCase):
    def testListOfZeros(self):
        self.assertEqual(retornaIndices([0,0,0,0,], 15), [0, 0])
