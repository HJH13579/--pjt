from rest_framework.serializers import ModelSerializer
from ..models import Review, Movie


class ReviewListSerializer(ModelSerializer):
    class MovieForReview(ModelSerializer):
        class Meta:
            model = Movie
            fields = ['title']
    movie = MovieForReview(read_only=True)
    class Meta:
        model = Review
        fields = ['id',  'movie', 'title', 'content']
        read_only_fields = ['movie']
