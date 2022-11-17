from django.urls import path
from .views import VendaList , VendaMethodObject

urlpatterns = [
    path('vendas/', VendaList.as_view()),
    path('venda/<int:id>/', VendaMethodObject.as_view())
    
]