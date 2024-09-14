from rest_framework import serializers
from subtasks.models import SubTask


class SubtaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = '__all__'
