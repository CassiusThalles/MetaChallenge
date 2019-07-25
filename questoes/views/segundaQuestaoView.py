from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import verificaSeStringEBalanceada

class SegundaQuestao(APIView):
    def post(self, request):
        requisicao = request.data
        stringBalanceada = verificaSeStringEBalanceada.balanceada(requisicao["sequencia"])
        resposta = {
            "input": requisicao["sequencia"],
            "output": stringBalanceada
        }
        return Response(resposta)