import requests
from pprint import pprint

import os
from dotenv import load_dotenv

load_dotenv()

private_key = os.environ.get('api_key')

def ranking():
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={private_key}' # TMBD의 Get Popular 

    response = requests.get(URL).json() 

    lst_popular_movie = response.get('results') # 유명 영화 정보들이 리스트 안의 딕셔너리 형태로 포함
    
    vote_lst = [] # 평점만 모아놓은 리스트

    for movie in lst_popular_movie:
        vote_lst.append(movie.get('vote_average'))

    top_vote_lst = sorted(vote_lst, reverse = True)[:5] # 가장 평점이 높은 5개만 골라서 새로운 리스트 생성

    top_vote_movies = [] # 가장 평점이 높은 5개의 영화 정보를 담기 위한 리스트

    for i in range(5):  # 중첩 for문 순서 주의!!! 
        for movie in lst_popular_movie: # 반대로 할 시 : 각 movie 딕셔너리의 평점마다 5개의 평점을 비교함. 결국 'movie.get('vote_average') in top_vote_lst'하고 같아짐. 평점 높은 순서대로 X
            if movie.get('vote_average') == top_vote_lst[i]:
                if movie in top_vote_movies:
                    pass
                else:
                     top_vote_movies.append(movie)

    return top_vote_movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
