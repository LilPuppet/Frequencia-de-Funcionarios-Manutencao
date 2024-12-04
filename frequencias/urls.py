from django.urls import path
from . import views  # Substitua por imports adequados

urlpatterns = [
    # Exemplo de rota
    path("", views.FrequenciaListView.as_view(), name="frequencias-list"),
]
