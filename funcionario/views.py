from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Funcionario, Setor
from .serializers import SetorSerializer, FuncionarioSerializer
from django.views.decorators.csrf import csrf_exempt

class FuncionarioList(APIView):
    '''
    Meotodo HTTP GET ALL, POST OBJECT
    '''
    
    def get(self, request):
        funcionario = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionario, many=True)
        return Response(serializer.data)
    
    
    @csrf_exempt
    def post(self,request):
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class FuncionarioMethodObject(APIView):
    '''
    Metodo HTTP - GET Object, PUT, DELETE
    '''
    
    def get_object(self,id):
        try:
            return Funcionario.objects.get(id=id)
        except:
            raise Http404
    
    def get(self,request,id):
        funcionario = self.get_object(id)
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)
    
    def put(self,request,id):
        funcionario = self.get_object(id)
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        funcionario = self.get_object(id)
        funcionario.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
        
    

# Create your views here.
