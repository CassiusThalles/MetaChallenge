from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import retornaIndices

class PrimeiraQuestao(APIView):
    def post(self, request, format=None):
        requisicao = request.data
        indices = retornaIndices.retornaIndices(requisicao["lista"], requisicao["alvo"])
        resposta = {
            "lista": requisicao["lista"],
            "alvo": requisicao["alvo"],
            "resposta": indices
        }
        return Response(resposta)