from rest_framework import serializers
from .models import IdeaBox


class IdeaBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaBox
        fields = '__all__'
