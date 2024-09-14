from rest_framework.serializers import ModelSerializer
from ai.models import AIResult


class AISerializer(ModelSerializer):

    class Meta:
        model = AIResult
        fields = ['result',]
