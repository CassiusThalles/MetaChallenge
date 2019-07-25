from django.urls import path
from questoes.views import primeiraQuestaoView,segundaQuestaoView, terceiraQuestaoView, quartaQuestaoView

urlpatterns = [
    path('questao01/', primeiraQuestaoView.PrimeiraQuestao.as_view()),
    path('questao02/', segundaQuestaoView.SegundaQuestao.as_view()),
    path('questao03/', terceiraQuestaoView.TerceiraQuestao.as_view()),
    path('questao04/', quartaQuestaoView.QuartaQuestao.as_view()),
]