from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Blog, Category
from blog.serializers import BlogSerializer, CategorySerializer
from main.models import Task
from rest_framework import viewsets
from main.serializers import TaskSerializer


# class TaskViewSet(viewsets.ViewSet):

#     def list(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many = True)
#         return Response(serializer.data, 200)

#     def create(self, request):
#         item = TaskSerializer(data=request.data)
#         if item.is_valid():
#             item.save()
#             return Response(item.data, 201)
#         else:
#             return Response({'error': item.errors},status=400)
    
#     def destroy(self, request, pk=None):
#         task = Task.objects.get(pk=pk)
#         task.delete()
#         return Response(status=400)

#     def update(self, request, pk=None):
#         item = Task.objects.get(id=pk)
#         items = TaskSerializer(instance=item, data=request.data)
#         if items.is_valid():
#             items.save()
#             return Response(items.data, status=200)
#         else:
#             return Response({'error': items.errors}, status=200)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ListTask(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all()
        sezializer = TaskSerializer(tasks, many=True)
        return Response(sezializer.data, 200)
    

class BlogViewSet(viewsets.ViewSet):

    def list(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many = True)
        return Response(serializer.data, 200)

    def create(self, request):
        blog = BlogSerializer(data=request.data)
        if blog.is_valid():
            blog.save()
            return Response(blog.data, 201)
        else:
            return Response({'error': blog.errors},status=400)
    
    def destroy(self, request, pk=None):
        task = Blog.objects.get(pk=pk)
        task.delete()
        return Response(status=400)

    def update(self, request, pk=None):
        item = Blog.objects.get(id=pk)
        items = BlogSerializer(instance=item, data=request.data)
        if items.is_valid():
            items.save()
            return Response(items.data, status=200)
        else:
            return Response({'error': items.errors}, status=200)
        
class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data, 200)

    def create(self, request):
        item = CategorySerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(item.data, 201)
        else:
            return Response({'error': item.errors},status=400)
    
    def destroy(self, request, pk=None):
        task = Category.objects.get(pk=pk)
        task.delete()
        return Response(status=400)

    def update(self, request, pk=None):
        item = Category.objects.get(id=pk)
        items = CategorySerializer(instance=item, data=request.data)
        if items.is_valid():
            items.save()
            return Response(items.data, status=200)
        else:
            return Response({'error': items.errors}, status=200)