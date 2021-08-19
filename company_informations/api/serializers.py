from rest_framework import serializers
from company_informations import models

class SectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Sectors
        fields = '__all__'