import json
# import os

def max_revenue(movies):

    # path = "./data/movies"
    # file_lst = os. listdir(path)
    # print(file_lst)

    # for file in file_lst:
    #     movie_json = json.load(open('data/movies/' + file, encoding='utf-8'))
    #     print(movie_json)

    lst_revenue = []

    for movie in movies:
        id = movie['id']
        open_file = json.load(open(f'data/movies/{id}.json', encoding='utf-8'))

        rev = open_file['revenue']
        lst_revenue.append(rev)
    
    max_revenue_cost = sorted(lst_revenue, reverse=True)[0]
    
    for movie in movies:
        id = movie['id']
        open_file = json.load(open(f'data/movies/{id}.json', encoding='utf-8'))

        if max_revenue_cost == open_file['revenue']:
            max_revenue_name = open_file['title']

    return max_revenue_name
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))


