from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters

from .models import Task
from .persmissions import IsAuthorOrReadOnly, IsAdminUser
from .serializers import TaskSerializer, UserSerializer

# Create your views here.    
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer