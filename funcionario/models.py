from django.db import models

# Create your models here.

class Setor(models.Model):
    TIPOS_CHOICE =[
        (1,'Vendas Externas'),
        (2,'Vendas Internas'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.IntegerField(choices=TIPOS_CHOICE)
    
    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
    
    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.PositiveIntegerField()
    data_nascimento = models.DateField(auto_now=False)
    setor = models.ForeignKey(Setor,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
    
    def __str__(self):
        return self.nome
        
    
