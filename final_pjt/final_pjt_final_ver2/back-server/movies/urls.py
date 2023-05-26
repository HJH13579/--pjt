from django.urls import path
from . import views
app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:movie_id>/comments/', views.movie_comments, name='movie_comments'),
    path('<int:movie_id>/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    
]