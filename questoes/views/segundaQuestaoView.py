from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import verificaSeStringEBalanceada
from rest_framework import status

class SegundaQuestao(APIView):
    def post(self, request):
        try:
            requisicao = request.data
            stringBalanceada = verificaSeStringEBalanceada.balanceada(requisicao["sequencia"])
            resposta = {
                "input": requisicao["sequencia"],
                "output": stringBalanceada
            }
            return Response(resposta, status.HTTP_200_OK)
        except:
            requisicao = request.data
            return Response(requisicao, status.HTTP_400_BAD_REQUEST)