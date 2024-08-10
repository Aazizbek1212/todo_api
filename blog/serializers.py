from rest_framework import serializers

from blog.models import Blog, Category




class BlogSerializer(serializers.Serializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'