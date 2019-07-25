from django.urls import path, include

urlpatterns = [
    path('', include("questoes.routes.urls")),
]
