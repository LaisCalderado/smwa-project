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
            student = Student.objects.get(studentId=pk)
            return student
        except:
            return JsonResponse("Student Does Not Exist", safe=False)

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else:
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Created Successfully", safe=False)
        return JsonResponse("Failed to Add Student", safe=False)

    def put(self, request, pk=None):
        student_to_update = Student.objects.get(studentId=pk)
        serializer = StudentSerializer(instance=student_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Student")

    def delete(self, request, pk=None):
        student_to_delete = Student.objects.get(studentId=pk)
        student_to_delete.delete()
        return JsonResponse("Student Deleted Successfully", safe=False)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': 'User registered successfully'})
    return JsonResponse({'message': 'Invalid request method'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'})
    return JsonResponse({'message': 'Invalid request method'})




