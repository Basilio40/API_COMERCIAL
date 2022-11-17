from django.urls import path
from .views import ClienteList , ClienteMethodObject

urlpatterns = [
    path('clientes/', ClienteList.as_view()),
    path('cliente/<int:id>/', ClienteMethodObject.as_view())
    
]