from rest_framework import serializers
from .models import Venda, Vendas_Prod

class VendasProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendas_Prod
        fields = '__all__'
        
class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'