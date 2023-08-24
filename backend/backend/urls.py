from django.contrib import admin
from django.urls import path, include

from .views import UserCreateView

from rest_framework import routers
route = routers.DefaultRouter()
from students.api import viewsets as ProfileViewset

from .views import CustomTokenObtainPairView


route.register(r'students', ProfileViewset.StudentViewSet , basename="Students")
route.register(r'perfils', ProfileViewset.ProfileViewset, basename="Perfils")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(route.urls)),
]

