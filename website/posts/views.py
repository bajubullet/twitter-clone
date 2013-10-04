from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import viewsets

from models import Post
from serializers import PostSerializer


@api_view(['GET',])
def api_root(request, format=None):
  return Response({
      'posts': reverse('post-list', request=request, format=format)
  })


class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  def pre_save(self, obj):
    obj.author = self.request.user

  def get_queryset(self):
    return Post.objects.filter(author=self.request.user)


class PostList(APIView):
  """
  List all posts, or create a new post.
  """
  def get(self, request, format=None, username=None):
    if username:
      posts = Post.objects.filter(author__username=username)
    else:
      posts = Post.objects.filter(author__in=request.user.users_following)
    serializer = PostSerializer(posts.order_by('-timestamp'), many=True)
    return Response(serializer.data)
