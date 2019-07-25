from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import retornaLucroMaximo

class TerceiraQuestao(APIView):

    def post(self, request):
        requisicao = request.data
        lucroMaximo = retornaLucroMaximo.retornaValorMaximo(requisicao["input"])
        resposta = {
            "input": requisicao["input"],
            "Lucro Máximo": lucroMaximo
        }
        return Response(resposta)