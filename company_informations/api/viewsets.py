from rest_framework import viewsets
from company_informations.api import serializers
from company_informations import models

class SectorsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SectorsSerializer
    queryset = models.Sectors.objects.all()