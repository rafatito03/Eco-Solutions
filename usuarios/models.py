from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    is_avaliador = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - Avaliador: {'Sim' if self.is_avaliador else 'Não'}"

class ONG(models.Model):
    nome = models.CharField(max_length=255,default='ONG')
    cnpj = models.CharField(max_length=18, default='00.000.000/0001-00')
    endereco = models.CharField(max_length=255,null=True, blank=True,default='Rua')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    informacao = models.TextField(blank=True, null=True)
    imagem = models.CharField(max_length=1000, null=True, blank=True, default='imagens/rick_roll.jpg')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ong',null=True)

    def __str__(self):
        return self.nome

class Residuos(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='residuos')
    tipo = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    peso = models.FloatField(blank=True, null=True)
    status = models.CharField(
        max_length=50, 
        choices=[('armazenado', 'Armazenado'), ('reciclado', 'Reciclado'), ('descartado', 'Descartado')]
    )
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.quantidade} unidades"
    
class AvaliacaoONG(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('ong', 'usuario')

    def __str__(self):
        return f"{self.ong.nome} - {self.nota} ({self.usuario.username})"
    
class RemoverAvaliacao(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='remover_avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remover_avaliacoes')

    class Meta:
        unique_together = ('ong', 'usuario')

    def __str__(self):
        return f"{self.ong.nome} - {self.usuario.username}" 
    
class EditarAvaliacao(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name='editar_avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editar_avaliacoes')

    class Meta:
        unique_together = ('ong', 'usuario')

    def __str__(self):
        return f"{self.ong.nome} - {self.usuario.username}" 

class Armazenamento(models.Model):
    ong = models.ForeignKey('ONG', on_delete=models.CASCADE)
    tipo_tecido = models.CharField(max_length=100)
    metros = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo_tecido} - {self.metros}m ({self.ong.nome})"