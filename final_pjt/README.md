# 메인페이지

## 프로젝트 설정
cd back-server
cd front-server

<BackEnd>
python -m venv venv  #가상환경 생성

source venv/Scripts/activate  #가상환경 활성화

pip install -r requirements.txt

pip freeze > requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py loaddata movies/movie_data.json

python manage.py runserver

<FrontEnd>

pip install i 
pip install django-cors-headers
pip install dj-rest-auth
pip install 'dj-rest-auth[with_social]'
npm install vue bootstrap-vue bootstrap

npm run serve

## 참고한 프로젝트들
- https://github.com/SSAFY-5th-seungwoon/Moya_backend
- https://github.com/team-amu/amu

## 제작 순서
1. 스케치 (Figma)
2. ERD (1:M, N:M) (Erdcloud)
3. BackEnd (Postman을 통해 확인)
   - GET을 하는 기능은 로그인 없이 기능
   - POST, DELETE 기능은 로그인 해야 기능하도록
4. FrontEnd
5. 무료 서버에 올리기 (동기 비동기 처리의 중요성)

## 구상
- '현재상영작', '상영예정작', '평점 높은 영화', '유명한 영화'의 영화 포스터들을 가로 스크롤 방식으로 보여주기
- 5~7개의 영화 포스터를 주고, Next/Prev 화살표 버튼을 통해 다른 포스터들을 보여주기
- 일정 시간이 지나면 자동으로 다음 리스트의 포스터들로 넘어가기
- 첫/마지막 페이지에서 더 넘어가려고 할 시 마지막/첫 페이지로 자연스럽게 넘어가기 (Loop)

## 구현
- 실시간으로 변경되는 정보들이기에, DB에서가 아닌 API를 통해 Data 받아오기
- 가로 스크롤을 가장 자연스럽게 구현 가능한 Bootstrap의 'carousel'과 Vue를 합친 라이브러리 'vue-carousel'를 이용해서 구현

## 문제점
- 'vue-carousel' 라이브러리가 제공하는 ':loop'는 이전/다음 슬라이들을 빠르게 skip하는 방식으로, skip되는 과정이 눈에 보인다.

## 개선점
- 자연스러운 Loop 구현
- 화살표 모양, 색상
- 포스터 크기 조정, 가로/세로 길이 변경
- 시간이 지나면 자동으로 다음 리스트의 포스터들로 넘어가기



# 포스터 클릭 시 Detail 링크로 이동






# 오리지널 티켓 만들기

## 구상
- CSS로 틀을 잡고, 거기에 포스터를 합친다.
  - 최대한 틀과 포스터의 중앙을 맞춘다.
  - 각 모서리에 좀 큰 1/4 원으로 펀칭, 짧은 변인 폭에 7개의 작은 반원 펀칭

## 문제점
- CSS가 상상 이상으로 불친절, 손이 많이 감
  - 그렇다고 JavaScript하고 같이 쓰긴 좀....그렇고.....