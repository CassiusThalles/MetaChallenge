from rest_framework.response import Response
from rest_framework.views import APIView
from questoes.views.funcoes import calcularVolumeDeChuva

class QuartaQuestao(APIView):

    def post(self, request, format=None):
        requisicao = request.data
        volumeDeChuva = calcularVolumeDeChuva.calcularVolumeDeChuva(requisicao["lista"])
        resposta = {
            "input": requisicao["lista"],
            "Volume de chuva retida": volumeDeChuva
        }
        return Response(resposta)