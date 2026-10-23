from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'