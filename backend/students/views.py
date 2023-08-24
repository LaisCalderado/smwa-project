from rest_framework.views import APIView
from .serializers import StudentSerializer
from django.http.response import JsonResponse
from .models import Student
from django.http.response import Http404
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import json


class StudentView(APIView):
    def get_student(self, pk):
        try:
            return Student.objects.get(studentId=pk)
        except Student.DoesNotExist:
            raise Http404("Student does not exist")

    def get(self, request, pk=None):
        if pk:
            student = self.get_student(pk)
            serializer = StudentSerializer(student)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Created Successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        student = self.get_student(pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Updated Successfully")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        student = self.get_student(pk)
        student.delete()
        return Response("Student Deleted Successfully", status=status.HTTP_204_NO_CONTENT)




