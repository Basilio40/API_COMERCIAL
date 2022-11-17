from django.db import models


class Endereco(models.Model):
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
    
    def __str__(self):
        return self.endereco

class Cliente(models.Model):
    SEXO_CHOICE = [
        (1,'Masculino'),
        (2,'Feminino'),
    ]
    TIPO_CHOICE = [
        (1, 'Pessoa Ficica'),
        (2, 'Pessoa Juridica'),
    ]
    nome= models.CharField(max_length=100)
    sexo = models.IntegerField(choices=SEXO_CHOICE)
    data_nasc = models.DateField(auto_now=False)
    endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE)
    telefone = models.CharField(max_length=25) # (11) 99XXX-8XXX
    tipo = models.IntegerField(choices=TIPO_CHOICE)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nome
