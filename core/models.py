from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Postagem(models.Model):
    titulo = models.CharField(max_length=30, default="Sem Titulo", null=False, blank=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now=True)
    publico = models.BooleanField()

    class Meta:
        db_table = 'postagens'

    def __str__(self):
        if self.titulo:
            return self.titulo
        else:
            return "Sem Titulo"
    
    def get_postagem_publica(self):
        if self.publico:
            return False
        else:
            return True
