from rest_framework import viewsets, status
from rest_framework.response import Response
from students import serializers
from students import models

# autenticação
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProfileViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PerfilSerializer
   
    # para filtrar por id do user
    def get_queryset(self):
        # Obtém o valor do parâmetro 'user' da URL
        id_user = self.request.query_params.get('user', None)
        if id_user:
            # Filtra os Perfils por 'user' caso seja fornecido na URL
            queryset = models.Profile.objects.filter(user=id_user)
        else:
            # Caso 'user' não seja fornecido, retorna todos os produtos
            queryset = models.Profile.objects.all()
        return queryset

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Created Successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Student Updated Successfully")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response("Student Deleted Successfully", status=status.HTTP_204_NO_CONTENT)