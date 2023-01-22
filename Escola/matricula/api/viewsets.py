from rest_framework import viewsets
from matricula import models
from matricula.api import serializers


class MatriculaViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.MatriculaSerializer
    queryset = models.Matricula.objects.all()


class MatriculaViewSetOut(viewsets.ModelViewSet):
    serializer_class = serializers.MatriculaSerializerOut

    def get_queryset(self):
        ra = self.request.query_params.get('ra')

        if ra == None:
            return models.Matricula.objects.all()
        else:
            return models.Matricula.objects.filter(alunos_ra=ra)