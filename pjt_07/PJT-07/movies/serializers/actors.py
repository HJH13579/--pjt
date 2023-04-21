from rest_framework.serializers import ModelSerializer
from ..models import Actor, Movie


class ActorListSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']


class ActorDetailSerializer(ActorListSerializer):
    class MovieForActorDetail(ModelSerializer):
        class Meta:
            model = Movie
            fields = ['title']

    movies = MovieForActorDetail(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['id', 'movies', 'name']
        

