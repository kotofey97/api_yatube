from rest_framework import serializers
from rest_framework.serializers import SlugRelatedField

from posts.models import Comment, Group, Post

class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Post
        fields =  '__all__'


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields =  '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Comment
        fields = '__all__'
