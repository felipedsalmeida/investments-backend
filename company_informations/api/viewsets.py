from rest_framework import viewsets
from company_informations.api import serializers
from company_informations import models

class SectorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SectorSerializer
    queryset = models.Sector.objects.all()

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.CompanySerializer
    queryset = models.Company.objects.all()