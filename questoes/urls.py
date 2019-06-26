from django.urls import path
from questoes import views

urlpatterns = [
    path('questao01/', views.PrimeiraQuestao.as_view()),
    path('questao02/', views.SegundaQuestao.as_view()),
    path('questao03/', views.TerceiraQuestao.as_view()),
    path('questao04/', views.QuartaQuestao.as_view()),
]