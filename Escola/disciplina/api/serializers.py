from rest_framework import serializers
from disciplina import models


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ['nome','carga_horaria']


class DisciplinaSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina
        fields = ['nome']
