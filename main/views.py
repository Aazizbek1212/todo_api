from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Task
from rest_framework import viewsets
from main.serializers import TaskSerializer


class TaskViewSet(viewsets.ViewSet):

    def list(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data, 200)

    def create(self, request):
        item = TaskSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(item.data, 201)
        else:
            return Response({'error': item.errors},status=400)
    
    def destroy(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=400)

    def update(self, request, pk=None):
        item = Task.objects.get(id=pk)
        items = TaskSerializer(instance=item, data=request.data)
        if items.is_valid():
            items.save()
            return Response(items.data, status=200)
        else:
            return Response({'error': items.errors}, status=200)