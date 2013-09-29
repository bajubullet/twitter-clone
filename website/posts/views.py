from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from models import Post
from permissions import IsOwner
from serializers import PostSerializer


@api_view(['GET',])
def api_root(request, format=None):
  return Response({
      'posts': reverse('post-list', request=request, format=format)
  })


class PostList(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  def get_queryset(self):
    return Post.objects.filter(author=self.request.user)


class PostDetail(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = (IsOwner,)