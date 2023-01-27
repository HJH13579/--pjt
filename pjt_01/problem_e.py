import json


def dec_movies(movies):
    
    lst_dec_movies = []

    for movie in movies:
        id = movie['id']
        open_file = json.load(open(f'data/movies/{id}.json', encoding='utf-8'))

        month_movie = open_file['release_date']
        title_movie = open_file['title']

        if month_movie[5:7] == '12':
            lst_dec_movies.append(title_movie)

    return lst_dec_movies
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

