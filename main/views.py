from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Task
from main.serializers import TaskSerializer



@api_view(['GET'])
def todo_list_view(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data, 200)


@api_view(['POST'])
def add_item_view(request):
    item = TaskSerializer(data=request.data)

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=200)


@api_view(['POST'])
def update_todo_view(request, pk):
    item = Task.objects.get(id=pk)
    data = TaskSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data, 200)
    else:
        return Response(status=200)