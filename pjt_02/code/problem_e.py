import requests
from pprint import pprint

import os
from dotenv import load_dotenv

load_dotenv()

private_key = os.environ.get('api_key')

def credits(title):
    try:
        URL1 = f'https://api.themoviedb.org/3/search/movie?api_key={private_key}&query={title}' # TMDB에서 영화 검색

        response1 = requests.get(URL1).json() # 딕셔너리 안의 리스트의 딕셔너리

        first_id = (response1.get('results')[0]).get('id') # 딕셔너리 안의 'results' value값(영화 정보들)의 리스트 중 첫번째 딕셔너리(첫번째 영화)의 'id'

        URL2 = f'https://api.themoviedb.org/3/movie/{first_id}/credits?api_key=db499efb2cc0ba6f9698b4699f1b762e' # 딕셔너리

        response2 = requests.get(URL2).json().get('cast') # 딕셔너리 key 'cast'의 value는 리스트(안에 직원 정보 딕셔너리 존재)
        response3 = requests.get(URL2).json().get('crew')

        cast_list = []

        directing_list = []

        for cast in response2:
            if cast.get('cast_id') < 10:
                cast_list.append(cast.get('name'))

        for cast in response3:
            if cast.get('department') == 'Directing':
                directing_list.append(cast.get('name'))

        return cast_list, directing_list

    except IndexError:
        return None

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
