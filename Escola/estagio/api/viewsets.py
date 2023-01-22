from rest_framework import viewsets
from estagio import models
from estagio.api import serializers


class EstagioViewSet(viewsets.ModelViewSet):
    queryset = models.Estagio.objects.all()
    serializer_class = serializers.EstagioSerializer