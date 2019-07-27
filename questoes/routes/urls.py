from django.urls import path
from questoes.views import primeiraQuestaoView,segundaQuestaoView, terceiraQuestaoView, quartaQuestaoView

urlpatterns = [
    path('questao01/', primeiraQuestaoView.PrimeiraQuestao.as_view(), name='questao01'),
    path('questao02/', segundaQuestaoView.SegundaQuestao.as_view(), name='questao02'),
    path('questao03/', terceiraQuestaoView.TerceiraQuestao.as_view(), name='questao03'),
    path('questao04/', quartaQuestaoView.QuartaQuestao.as_view(), name='questao04'),
]