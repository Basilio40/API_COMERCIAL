from django.urls import path
from .views import ProdutoList , ProdutoMethodObject

urlpatterns = [
    path('produtos/', ProdutoList.as_view()),
    path('produto/<int:id>/', ProdutoMethodObject.as_view())
    
]