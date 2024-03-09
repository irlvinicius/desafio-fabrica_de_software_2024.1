from rest_framework.serializers import ModelSerializer

from ..models import Pais

class PaisSerializer(ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id','name','capital','subregion','population','region']