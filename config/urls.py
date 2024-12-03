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
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from frequencias.api.views import FrequenciaViewSet
from users.api.views import FuncionarioViewSet, UserProfileExampleViewSet
from users.views import LoginView

router = SimpleRouter()

router.register("users", UserProfileExampleViewSet, basename="users")
router.register("funcionarios", FuncionarioViewSet, basename="funcionarios")
router.register("frequencia", FrequenciaViewSet, basename="Frequências")



urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('login/', LoginView.as_view(), name='login'),
]+router.urls
