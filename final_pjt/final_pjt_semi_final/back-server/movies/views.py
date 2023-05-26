from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_comments(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    comments = Comment.objects.filter(movie=movie)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "로그인해주세요ㅠㅠ"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({"detail": "로그인해주세요ㅠㅠ"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['post'])
@permission_classes([IsAuthenticated])
def comment_like(request, movie_id, comment_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    comment = get_object_or_404(Comment,pk=comment_id)
    user = request.user
    if comment.user_id != user:
        if comment.like_users.filter(pk=user.pk).exists():
            comment.like_users.remove(user)
            follow = False
        else:
            comment.like_users.add(user)
            follow = True

        comment.save()
        
        follow_status ={
            'follow':follow,
            'count':comment.like_users.count(),
        }
        return JsonResponse(follow_status)