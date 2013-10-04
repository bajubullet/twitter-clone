from rest_framework import serializers

from models import Post


class PostSerializer(serializers.ModelSerializer):
  author_full_name = serializers.Field(source='author.get_full_name')
  author_username = serializers.Field(source='author.username')
  author_photo = serializers.Field(source='author.photo_url')
  class Meta:
    model = Post
    fields = ('id', 'content', 'timestamp', 'author_full_name', 'author_username',
              'author_photo')
