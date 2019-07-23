from rest_framework.views import APIView
from rest_framework.response import Response
import json

class PrimeiraQuestao(APIView):
    def post(self, request, format=None):
        requisicao = request.data
        indices = self.retornaIndices(requisicao["lista"], requisicao["alvo"])
        resposta = {
            "lista": requisicao["lista"],
            "alvo": requisicao["alvo"],
            "resposta": indices
        }
        return Response(resposta)
    
    #Estou considerando que dada a lista e o alvo, a pergunta tenha solução
    def retornaIndices(self, lista: list, alvo: int):
        mydict = {}
        for i in list(range(len(lista))):
            mydict.update({lista[i]: i})

        for i in list(range(len(lista))):
            diferenca = alvo - lista[i]
            if diferenca in mydict.keys():
                return [i, mydict[diferenca]]
        
        return [0, 0]

class SegundaQuestao(APIView):
    def post(self, request, format=None):
        requisicao = request.data
        stringBalanceada = self.balanceada(requisicao["sequencia"])
        resposta = {
            "input": requisicao["sequencia"],
            "output": stringBalanceada
        }
        return Response(resposta)
    
    def balanceada(self, sequencia: list):
        valorauxiliar = len(sequencia)/2
        valorauxiliar = int(valorauxiliar)
        resposta = "SIM"
        for i in reversed(range(valorauxiliar)):
            if(sequencia[i] == "("):
                if(sequencia[2*valorauxiliar-i-1] != ")"):
                    resposta = "NÃO"
                    break
            if(sequencia[i] == "["):
                if(sequencia[2*valorauxiliar-i-1] != "]"):
                    resposta = "NÃO"
                    break
            if(sequencia[i] == "{"):
                if(sequencia[2*valorauxiliar-i-1] != "}"):
                    resposta = "NÃO"
                    break
        return resposta

class TerceiraQuestao(APIView):

    def post(self, request, format=None):
        requisicao = request.data
        lucroMaximo = self.retornaValorMáximo(requisicao["input"])
        resposta = {
            "input": requisicao["input"],
            "Lucro Máximo": lucroMaximo
        }
        return Response(resposta)
    
    def retornaValorMáximo(self, input):
        variacaoDeValor = []
        for i in range(1, len(input)):
            valorAuxiliar = input[i] - input[i-1]
            variacaoDeValor.append(valorAuxiliar)
        lucroMaximo = 0
        contador = 0
        for i in range(len(variacaoDeValor)):
            if(contador + variacaoDeValor[i] >= contador):
                contador = contador + variacaoDeValor[i]
            if(contador + variacaoDeValor[i] < contador):
                if(contador + variacaoDeValor[i] > 0):
                    contador = contador + variacaoDeValor[i]
                else:
                    contador = 0
            if(contador > lucroMaximo):
                lucroMaximo = contador
        return lucroMaximo

class QuartaQuestao(APIView):

    def post(self, request, format=None):
        requisicao = request.data
        volumeDeChuva = self.CalcularVolumeDeChuva(requisicao["lista"])
        resposta = {
            "input": requisicao["lista"],
            "Volume de chuva retida": volumeDeChuva
        }
        return Response(resposta)
    
    def CalcularVolumeDeChuva(self, minhaLista):
        maiorAltura = max(minhaLista)
        mapeamento = [0] * maiorAltura
        maiorAlturaAlcancada = 0
        volumeDeChuva = 0
        for i in range(len(minhaLista)):
            if(i > 0 and minhaLista[i] > minhaLista[i-1]):
                for j in range(minhaLista[i-1], minhaLista[i]):
                    volumeDeChuva = volumeDeChuva + mapeamento[j]
                    mapeamento[j] = 0
            if(i>0 and minhaLista[i] < maiorAlturaAlcancada):
                for j in range(minhaLista[i], maiorAlturaAlcancada):
                    mapeamento[j] = mapeamento[j]+1
            if(minhaLista[i] > maiorAlturaAlcancada):
                maiorAlturaAlcancada = minhaLista[i]
        return volumeDeChuva
    