from rest_framework import serializers

from models import Post


class PostSerializer(serializers.ModelSerializer):
  author_full_name = serializers.Field(source='author.get_full_name')
  author_username = serializers.Field(source='author.username')
  author_photo = serializers.Field(source='author.photo_url')
  publish_date = serializers.Field(source='timestamp_in_millisecond')
  class Meta:
    model = Post
    fields = ('id', 'content', 'publish_date', 'author_full_name', 'timestamp',
              'author_username', 'author_photo')
