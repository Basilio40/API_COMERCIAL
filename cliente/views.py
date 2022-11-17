from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cliente, Endereco
from .serializers import ClienteSerializer, EnderecoSerializer
from django.views.decorators.csrf import csrf_exempt

class ClienteList(APIView):
    '''
    Meotodo HTTP GET ALL, POST OBJECT
    '''
    
    def get(self, request):
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class ClienteMethodObject(APIView):
    '''
    Metodo HTTP - GET Object, PUT, DELETE
    '''
    
    def get_object(self,id):
        try:
            return Cliente.objects.get(id=id)
        except:
            raise Http404
    
    def get(self,request,id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
    def put(self,request,id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        cliente = self.get_object(id)
        cliente.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
        
    
