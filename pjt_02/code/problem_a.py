import requests

import os
from dotenv import load_dotenv

load_dotenv()

private_key = os.environ.get('api_key')

def popular_count():
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={private_key}' # TMBD의 Get Popular 

    response = requests.get(URL).json() # 딕셔너리 형태로 받아옴

    num_movie = len(response.get('results')) # 딕셔너리 안에 'page'와 'results'가, 그리고 'results'안에 유명 영화 정보들이 리스트 안의 딕셔너리 형태로 포함되어 있다.
                                             # 'results'의 value 값인 딕셔너리만 받아서 len 함수로 개수 확인

    return num_movie



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
