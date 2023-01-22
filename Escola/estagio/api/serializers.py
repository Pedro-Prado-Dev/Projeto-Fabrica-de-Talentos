from rest_framework import serializers
from estagio import models

class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estagio
        fields = '__all__'