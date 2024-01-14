from rest_framework.serializers import ModelSerializer
from .models import Make, Vechile


class MakeSerializer(ModelSerializer):
    class Meta:
        model = Make
        fields ='__all__'

class VechileSerializer(ModelSerializer):
    class Meta:
        model = Vechile
        fields ='__all__'