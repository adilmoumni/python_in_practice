from rest_framework import serializers
from .models import Employee2, Category, Ideabox


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee2
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class IdeaboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideabox
        fields = '__all__'
