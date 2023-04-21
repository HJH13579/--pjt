from rest_framework.serializers import ModelSerializer
from ..models import Movie, Actor

class MovieListSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'overview']


class MovieDetailSerializer(MovieListSerializer):
    class ActorForMovieDetail(ModelSerializer):
        class Meta:
            model = Actor
            fields = ['name']

    actors = ActorForMovieDetail(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'