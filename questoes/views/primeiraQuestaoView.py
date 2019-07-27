from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import retornaIndices
from rest_framework import status

class PrimeiraQuestao(APIView):
    def post(self, request):
        try:
            requisicao = request.data
            indices = retornaIndices.retornaIndices(requisicao["lista"], requisicao["alvo"])
            resposta = {
                "lista": requisicao["lista"],
                "alvo": requisicao["alvo"],
                "resposta": indices
            }
            return Response(resposta, status.HTTP_200_OK)
        except:
            requisicao = request.data
            return Response(requisicao, status.HTTP_400_BAD_REQUEST)
