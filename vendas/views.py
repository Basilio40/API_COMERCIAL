from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Venda, Vendas_Prod
from .serializers import VendaSerializer, VendasProdSerializer
from django.views.decorators.csrf import csrf_exempt

class VendaList(APIView):
    '''
    Meotodo HTTP GET ALL, POST OBJECT
    '''
    
    def get(self, request):
        venda = Venda.objects.all()
        serializer = VendaSerializer(venda, many=True)
        return Response (serializer.data)
    
    
    @csrf_exempt
    def post(self,request):
        serializer = VendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class VendaMethodObject(APIView):
    '''
    Metodo HTTP - GET Object, PUT, DELETE
    '''
    
    def get_object(self,id):
        try:
            return Venda.objects.get(id=id)
        except:
            raise Http404
    
    def get(self,request,id):
        venda = self.get_object(id)
        serializer = VendaSerializer(venda)
        return Response(serializer.data)
    
    def put(self,request,id):
        venda = self.get_object(id)
        serializer = VendaSerializer(venda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        venda = self.get_object(id)
        venda.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
        
    
from django.shortcuts import render

# Create your views here.
