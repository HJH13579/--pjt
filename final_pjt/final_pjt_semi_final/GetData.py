import requests
import json
import os

# TMDB_API_KEY = str(os.getenv('TMDB_API_KEY')) 환경변수 사용 안할 것
TMDB_API_KEY = 'db499efb2cc0ba6f9698b4699f1b762e'



def get_movie_datas():
    total_data = []

    # 1페이지부터 3페이지까지 (페이지당 20개, 총 60개)
    for i in range(1, 4):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    # 'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_movie_datas()
