import requests
from pprint import pprint

import os
from dotenv import load_dotenv

load_dotenv()

private_key = os.environ.get('api_key')

def recommendation(title):
    try:
        URL1 = f'https://api.themoviedb.org/3/search/movie?api_key={private_key}&query={title}' # TMDB에서 영화 검색

        response1 = requests.get(URL1).json() # 딕셔너리 안의 리스트의 딕셔너리

        first_id = (response1.get('results')[0]).get('id') # 딕셔너리 안의 'results' value값(영화 정보들)의 리스트 중 첫번째 딕셔너리(첫번째 영화)의 'id'

        URL2 = f'https://api.themoviedb.org/3/movie/{first_id}/recommendations?api_key=db499efb2cc0ba6f9698b4699f1b762e&language=ko'

        response2 = requests.get(URL2).json().get('results')

        lst_title = []

        for movie in response2:
            lst_title.append(movie.get('title'))

        return lst_title

    except IndexError:
        return None


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
