from rest_framework import serializers
from company_informations import models

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Sector
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Company
        fields='__all__'