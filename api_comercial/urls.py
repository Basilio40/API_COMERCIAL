
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('',include('cliente.urls')),
    path('',include('funcionario.urls')),
    path('',include('produto.urls')),
    path('',include('vendas.urls')),
]
