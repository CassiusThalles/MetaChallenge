from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import calcularVolumeDeChuva
from rest_framework import status

class QuartaQuestao(APIView):

    def post(self, request):
        try:
            requisicao = request.data
            volumeDeChuva = calcularVolumeDeChuva.calcularVolumeDeChuva(requisicao["lista"])
            resposta = {
                "input": requisicao["lista"],
                "Volume de chuva retida": volumeDeChuva
            }
            return Response(resposta, status.HTTP_200_OK)
        except:
            requisicao = request.data
            return Response(requisicao, status.HTTP_400_BAD_REQUEST)