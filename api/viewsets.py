from rest_framework import viewsets
from . import models
from . import serializers


class IdeaBoxViewset(viewsets.ModelViewSet):
    queryset = models.IdeaBox.objects.all()
    serializers_class = serializers.IdeaBoxSerializer
