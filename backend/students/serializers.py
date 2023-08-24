from rest_framework import serializers
from .models import Student
from students import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('studentId',
                  'FirstName',
                  'LastName',
                  'RegistrationNo',
                  'Email',
                  'Course')

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'
