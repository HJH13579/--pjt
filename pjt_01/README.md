# 관통프로젝트 1

## 요구사항 A
---
> 내용 정리
1. data 파일에 있는 'movie.json' 데이터('쇼생크 탈출'에 대한 정보)에서 필요 정보만 추출해 반환
2. 필요 정보 : 'genre_ids', 'id', 'overview', 'poster_path', 'title', 'vot_average' 순으로 
3. 새로운 딕셔너리 형태로 추출해 반환할 것

<br/>

> 문제
-  'movie.json'은 외부 데이터인데, 여기 있는 데이터를 어떻게 함수 안으로 끌고 들어올까....? (함수 안에 import해도 되나?)


> 해결책
- 일단 Python 내부에서는 어디서든 모듈은 한번만 import되기 때문에 어디서 import하든 상관없다.
- 오히려 함수 안에서 모듈을 import하는 것이 더 빠르나, Python 스타일 가이드 권장상 맨 위라고 한다.
- 쓸데없는 고민이었다. 맨 밑에서 이미 'movie_jason'을 가져와 주기 때문에, 나는 그저 필요한 데이터만 추출해서 정해진 형식으로만 출력하는 함수만 작성하면 되었다.
- open 함수는 함수를 생성하거나 열기 위한 함수로, open(file, mode, encoding 등) 여러 옵션을 가지고 있다. 
```python
movie_json = open('data/movie.json', encoding='utf-8')

# data 파일에 있는 'movie.json'을 UTF-8(유니코드)를 사용한 방식으로 인코딩 하겠다는 거다.
```
- JSON(JavaScript Object Notation) : 데이터를 문자열의 형태로 나타내기 위해서 사용
```python
json.load() # Json 파일을 Python 객체로 불러오기
```

## 요구사항 B
---

> 내용 정리
1. 이전 단계의 데이터 중 genre_ids를 장로 번호가 아닌 장르 이름 리스트 genre_names로 바꿔 반환하는 함수
2. genre_names 대신 genre_ids를 추출
3. genres.json을 이용하여 genre_ids를 각 장르 번호에 맞는 name 값으로 대체한 genre_names 키를 생성
4. 새로운 dictionary를 반환하는 함수 movie_info

--- 

> 문제

- 'genres.json을 이용하여 genre_ids를 각 장르 번호에 맞는 name 값으로
대체한 genre_names 키를 생성합니다.' 이 요구 사항 이해가 안 된다.
- 결국 기존의 dictionary의 key, value 모두 교체해야한다. Value 값이야 다시 새로 넣어주면 된다. 그런데 key 값은?
- Value 값이 리스트다. 리스트 안의 요소를 특정해서 교체하는게 생각보다 어렵다. 
- 'genres.json'이 리스트 안의 딕셔너리 형태다. 특정 키와 value값은 뽑아쓰는게 어렵다.
---

> 해결책
- 기존의 dictionary({key:value}={"genre_ids":[18, 80]})를 삭제하고 새로운 dictionarydictionary({key:value}={"genre_names":['drama', 'Crime']})로 교체하라는 소리였다.
- for _ in range(len())로 리스트 안 요소의 순서를 이용해 특정하자!
- 리스트 안의 딕셔너리는 for 구문으로 딕셔너리를 하나씩 뽑아서 비교하자. id 값이 일치하면, 기존 리스트 요소를 교체하고, 전부 다 교체하면, 'genre_ids'라는 키 이름을 pop 함수를 이용해 'genre_names'로 교체하자
- '교체'할 생각은 너무 어렵다. 차라리 새로운 리스트와 딕셔너리를 만들어서 거기다가 새로운 'genre_names' value들을 집어넣고, 기존의 딕셔너리를 지우는게 더 나은 방식일 수 있을 것 같다.

## 요구사항 C
---
> 내용 정리
1. movies.json에 20개의 평점 높은 영화 데이터
2. 서비스 구성에 필요한 정보만 추출해 반환하는 함수
3. 이전 단계의 함수 구조 재사용
4. 새로운 list를 반환하는 함수 movie_info
---
> 문제점
- 요구사항 a와 유사하고, 요구사항 b를 그대로 사용하나, 요구사항 a와의 차이라면 거긴 딕셔너리 하나, c는 딕셔너리를 담은 리스트라는 거다.
---

> 해결책
- 사실 b에서 고생해서 비교적 쉽게 해결. 리스트 안의 딕셔너리. 'movies_data'라는 빈 리스트 만들고, for 구문 돌려서 딕셔너리 모두를 요구사항 b로 세탁(?) 시킨 후 채워넣은 후 출력하자.


## 요구사항 D
---
> 내용 정리
1. 영화 세부 정보 중 수입 정보(revenue)를 이용
2. 모든 영화 중 가장 높은 수익을 낸 영화 출력
3. 반복문으로 movies 폴더 내부의 파일들을 오픈
4. 수익 같은 영화 없음
5. 수익이 가장 높은 영화 제목 출력 함수 max_revenue(original_title X , title 사용)
---
> 문제점
- 폴더 내부의 파일들을 어떻게 반복문으로 열 것인가.
- 반복문의 재탕(시간 관계상) 

---
> 해결책
- 원래는 os와 listdir 함수를 이용해서 풀려고 했으나 출제의도(id값으로 불러오기)와 맞지 않아서.....전면 수정
- 나중에 따로 title을 담은 리스트 만들어서 비교대조 후 최대 수익 나는 제목 가지고 오기


## 요구사항 E
---
> 내용 정리
1. 영화 세부 정보 중 개봉일 정보(release_data)를 이용
2. 모든 영화 중 12월에 개봉한 영화들 제목 리스트 출력

---
> 문제점
- 딱히 없었다. D의 약간의 변형

---
> 해결책