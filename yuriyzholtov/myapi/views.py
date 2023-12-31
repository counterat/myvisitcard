from django.core.exceptions import PermissionDenied
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hello.models import Post_blog, Works_blog
from .serializers import WorksBlogSerializer, PostBlogSerializer
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
def new_work(request):
    if request.headers.get('Token') == 'dkovsk0t94ri':
        try:    
            data = request.data
            title = data['title']
            description = data['description']
            category = data['category']
            photo_url = data['photo_url']
            post = Works_blog(title=title, content=description, images=[photo_url], category=category, created_at=datetime.now().year)
            post.save()
            return Response({'ok': 'yes'}, status=200)
        except Exception as ex:
            print(ex)
            return Response({'error': str(ex)}, status=400)
    raise PermissionDenied

@csrf_exempt
@api_view(['POST'])
def new_post(request):
    if request.headers.get('Token') == 'dkovsk0t94ri':
        try:
            data = request.data
            title = data['title']
            description = data['description']
            category = data['category']

            post = Post_blog(title=title, content=description, category=category, created_at=datetime.now().year)
            post.save()
            return Response({'ok': 'yes'}, status=200)
        except Exception as ex:
            return Response({'error': str(ex)}, status=400)
    raise PermissionDenied