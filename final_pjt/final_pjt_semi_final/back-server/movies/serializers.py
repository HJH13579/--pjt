from rest_framework import serializers
from .models import Movie, Comment
from accounts.serializers import UserDetailSerializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review','like_users',)

    def get_likes(self, obj):
        return obj.like_users.count() # 좋아요 개수를 반환