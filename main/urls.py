from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from main.views import TaskViewSet
from main.views import BlogViewSet, CategoryViewSet, ListTask


# router = DefaultRouter()
# router.register(r'task', TaskViewSet, basename='tasks')
router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename = 'blog')
router.register(r'category', CategoryViewSet, basename = 'category')

urlpatterns = [
    # path('', include(router.urls)),
    path('', include(router.urls)),
    path('tasks/', ListTask.as_view(), name='list'),
]
