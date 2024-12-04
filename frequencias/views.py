from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FrequenciaModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
