from django.db import models

class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereco=models.CharField(max_length=100,default="boate")
    latitude = models.FloatField()
    longitude = models.FloatField()
    informacao = models.TextField(blank=True, null=True)
    imagem = models.CharField(max_length=100, null=True, blank=True,default='imagens/rick_roll.jpg')
    

    def __str__(self):
        return self.nome
    
class Residuos(models.Model):
    tipo = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    peso = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('armazenado', 'Armazenado'), ('reciclado', 'Reciclado'), ('descartado', 'Descartado')])
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.quantidade} unidades"