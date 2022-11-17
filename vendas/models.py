from django.db import models
from funcionario.models import Funcionario
from cliente.models import Cliente
from produto.models import Produto


class Venda(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'
    
    def __str__(self):
        return str(self.funcionario)

class Vendas_Prod(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = 'Produto da venda'
        verbose_name_plural = 'Produtos da venda'
    
    def __str__(self):
        return str(self.venda)


