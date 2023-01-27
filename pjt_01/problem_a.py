import json
from pprint import pprint


def movie_info(movie):

    # [유지 보수 용이용 개선 Ver.]
    # lst = ['id', 'overview', 'genre_ids', 'poster_path', 'title', 'vote_average']
    # detail = {}
    # for key in lst:
    #     detail[key] = movie[key]

    movie_data = {
        'genre_ids': movie.get("genre_ids"), 
        'id': movie.get("id"), 
        'overview': movie.get("overview"), 
        'poster_path': movie.get("poster_path"),
        'title': movie.get("title"),
        'vote_average': movie.get("vote_average")
    }

    return movie_data


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))


