from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import TaskViewSet


router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
