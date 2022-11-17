from django.urls import path
from .views import FuncionarioList , FuncionarioMethodObject

urlpatterns = [
    path('funcionarios/', FuncionarioList.as_view()),
    path('funcionario/<int:id>/', FuncionarioMethodObject.as_view())
    
]