import json
from pprint import pprint


def movie_info(movies, genres):
    
    movies_data = []

    for movie in movies:
        movie_data = {
            'genre_ids': movie.get("genre_ids"), 
            'id': movie.get("id"), 
            'overview': movie.get("overview"), 
            'poster_path': movie.get("poster_path"),
            'title': movie.get("title"),
            'vote_average': movie.get("vote_average")
        }

        for i in range(len((movie.get("genre_ids")))):
            for diction in genres:
                if movie.get("genre_ids")[i] == diction["id"]:
                    movie.get("genre_ids")[i] = diction["name"]

        movie_data['genre_names'] = movie_data.pop('genre_ids')

        movies_data.append(movie_data)
    
    return movies_data
   
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
