"""
URL configuration for reservas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from frequencias.api.views import FrequenciaViewSet
from users.api.views import FuncionarioViewSetCreate, UserProfileExampleViewSet
from users.views import LoginView

# Configurando o router do DRF
router = SimpleRouter()
router.register("users", UserProfileExampleViewSet, basename="users")
router.register("funcionarios", FuncionarioViewSetCreate, basename="funcionarios")

router.register("frequencias", FrequenciaViewSet, basename="frequencias")  

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Autenticação
    path("api/token-auth/", views.obtain_auth_token),

    # Swagger e Schema
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    # Views manuais
    path("login/", LoginView.as_view(), name="login"),

    # Incluindo as URLs do app frequencias
    path("frequencias/", include("frequencias.urls")),  # Inclui URLs adicionais do app frequencias
]

# Adicionando as rotas do DRF
urlpatterns += router.urls
