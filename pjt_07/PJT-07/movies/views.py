from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Actor, Movie, Review
from .serializers.actors import ActorListSerializer, ActorDetailSerializer
from .serializers.movies import MovieDetailSerializer, MovieListSerializer
from .serializers.reviews import ReviewListSerializer

# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewListSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)


@api_view(['POST'])
def create_review(request, movie_pk):
    serializer = ReviewListSerializer(data=request.data)
    movie = Movie.objects.get(pk=movie_pk)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data)
