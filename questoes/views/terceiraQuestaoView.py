from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import retornaLucroMaximo
from rest_framework import status

class TerceiraQuestao(APIView):

    def post(self, request):
        try:
            requisicao = request.data
            lucroMaximo = retornaLucroMaximo.retornaValorMaximo(requisicao["input"])
            resposta = {
                "input": requisicao["input"],
                "Lucro Máximo": lucroMaximo
            }
            return Response(resposta, status.HTTP_200_OK)
        except:
            requisicao = request.data
            return Response(requisicao, status.HTTP_400_BAD_REQUEST)