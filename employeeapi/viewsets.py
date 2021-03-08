from rest_framework import viewsets
from . import models
from . import serializers


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee2.objects.all()
    serializer_class = serializers.EmployeeSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class IdeaboxViewset(viewsets.ModelViewSet):
    queryset = models.Ideabox.objects.all()
    serializer_class = serializers.IdeaboxSerializer
