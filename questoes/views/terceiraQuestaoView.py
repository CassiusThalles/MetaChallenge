from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import retornaValorMaximo

class TerceiraQuestao(APIView):

    def post(self, request, format=None):
        requisicao = request.data
        lucroMaximo = retornaValorMaximo.retornaValorMaximo(requisicao["input"])
        resposta = {
            "input": requisicao["input"],
            "Lucro Máximo": lucroMaximo
        }
        return Response(resposta)