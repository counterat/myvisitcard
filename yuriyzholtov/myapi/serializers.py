# serializers.py

from rest_framework import serializers
from hello.models import Post_blog, Works_blog

class WorksBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works_blog
        fields = '__all__'

class PostBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_blog
        fields = '__all__'
