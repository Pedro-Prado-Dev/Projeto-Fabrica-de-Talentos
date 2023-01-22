from rest_framework import viewsets
from professor import models
from professor.api import serializers


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = models.Professor.objects.all()
    serializer_class = serializers.ProfessorSerializer
