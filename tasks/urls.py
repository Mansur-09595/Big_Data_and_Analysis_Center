from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, TaskViewSet

router = SimpleRouter()

router.register('users', UserViewSet, basename='users'),
router.register('', TaskViewSet, basename='tasks'),

urlpatterns = router.urls