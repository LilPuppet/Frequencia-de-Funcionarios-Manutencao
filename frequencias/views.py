from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FrequenciaModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class FrequenciaListView(LoginRequiredMixin, ListView):
    model = FrequenciaModel
    template_name = "frequencias/frequencia_list.html"
    context_object_name = "frequencias"

class FrequenciaCreateView(LoginRequiredMixin, CreateView):
    model = FrequenciaModel
    template_name = "frequencias/frequencia_form.html"
    fields = ['hora_inicio', 'hora_fim', 'funcionario']
    success_url = reverse_lazy('frequencias:list')

class FrequenciaUpdateView(LoginRequiredMixin, UpdateView):
    model = FrequenciaModel
    template_name = "frequencias/frequencia_form.html"
    fields = ['hora_inicio', 'hora_fim', 'funcionario']
    success_url = reverse_lazy('frequencias:list')

class FrequenciaDeleteView(LoginRequiredMixin, DeleteView):
    model = FrequenciaModel
    template_name = "frequencias/frequencia_confirm_delete.html"
    success_url = reverse_lazy('frequencias:list')