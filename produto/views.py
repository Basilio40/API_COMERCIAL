from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categoria, Produto
from .serializers import ProdutoSerializer, CategoriaSerializer
from django.views.decorators.csrf import csrf_exempt



class ProdutoList(APIView):
    '''
    Meotodo HTTP GET ALL, POST OBJECT
    '''
    
    def get(self, request):
        produto = Produto.objects.all()
        serializer = ProdutoSerializer(produto, many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    def post(self,request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class ProdutoMethodObject(APIView):
    '''
    Metodo HTTP - GET Object, PUT, DELETE
    '''
    
    def get_object(self,id):
        try:
            return Produto.objects.get(id=id)
        except:
            raise Http404
    
    def get(self,request,id):
        cliente = self.get_object(id)
        serializer = ProdutoSerializer(cliente)
        return Response(serializer.data)
    
    def put(self,request,id):
        produto = self.get_object(id)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        produto = self.get_object(id)
        produto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
        
    
from django.shortcuts import render

# Create your views here.
