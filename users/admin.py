from django.contrib import admin # type: ignore

from users.models import Funcionario

# Register your models here.

admin.site.register(Funcionario)