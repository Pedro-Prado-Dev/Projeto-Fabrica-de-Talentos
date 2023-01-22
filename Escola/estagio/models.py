from django.db import models
from uuid import uuid1
# Create your models here.


class Estagio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    nome_empresa = models.CharField(max_length=45)
    cnpj_empresa = models.CharField(max_length=18)
    carga_horaria = models.IntegerField()
