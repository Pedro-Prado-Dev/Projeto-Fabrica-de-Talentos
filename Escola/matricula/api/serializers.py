from rest_framework import serializers
from aluno.api.serializers import AlunoSerializerOut
from disciplina.api.serializers import DisciplinaSerializerOut
from matricula import models


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Matricula
        fields = '__all__'


class MatriculaSerializerOut(serializers.ModelSerializer):
    alunos_ra = AlunoSerializerOut()
    disciplina_id = DisciplinaSerializerOut()

    class Meta:
        model = models.Matricula
        fields = ['npa','alunos_ra','disciplina_id']