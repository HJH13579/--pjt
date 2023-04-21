bㅠ# PJT - 07

> 처음 역활 분담
- Actor & Movie
  - Driver : 윤태영
  - Navigator : 허주혁
- Review
  - Driver : 허주혁
  - Navigator : 윤태영

---

- 사실 Pair Partner와의 수준 차이가 너무 나서, 사실상 가르침을 받는 시간이었다.
- 거의 다 Navigator 역활을 도맡아 했는데, 이는 Partner가 본인의 생각하는 힘과, 다음 step을 떠올리는 힘을 키워주기 위함이었으며, 막혔을 때 hint와 해결책을 제시해주는 방식으로 진행
- 본인을 위한 복습 시간이자, REST API를 더 깊게 학습할 수 있는 유익한 시간이었다.
- 파트너의 중요성을 새삼 느낌

</br>

## 코드 습관
1. 단계마다 모든 걸 만들고 다음 step으로 넘어가려고 한다.
   - function(구현, 구동) 단위로 코드를 짜는 것도 좋다.
   - 하나의 function을 모두 구현하고 다음 function으로 넘어가는 것도 고려
2. 필요한 게 나타났을 때 그 때마다 바로 만든다.
   - 공식화된 흐름을 따라가는 것이 아닌, 코드를 만들다 부족한 것이 있으면 그때 그때 만들어서 사용
3. 뭐가 필요한 지에 대한 명확한 targeting 필요
4. 변수 지칭의 명확화

</br>

## 착각
1. REST API는 BackEnd로, 철저히 데이터베이스를 다루는 function이다.
   - admin.py를 굳이 만들지 않아도, 제공되는 Admin Site를 이용할 수 있으며, 
   - 모델들(Actor, Movie, Review)도 등록되어 있고, 데이터의 생성, 조회, 수정, 삭제가 Serializer에 의해 적용된다.

2. 너무 더 나은 코딩에 연연하지 말자. 
   - 본인이 꼼수, 돌아가는 방법이라고 생각한 방법이 가장 이상적인 방법이거나, 답일 수 있다.
   - 일단 완성시켜 놓고, 더 나은 길을 찾자.

</br>

## 배운 점
1. 다른 class의 데이터를 받아와 표시하고 싶을 때는 상속 받아서 사용한다.
  
2. Serializer가 많아질 경우, 'serializer' 폴더 안에 '~.py', ...로 나눠서 분배해서 정리
   - 다만, 지금 프로젝트처럼 actor_detail에서 movie의 데이터를 필요로 해서 import를 해오고, movie_detail에서 actor의 데이터를 필요로 해서 import 해오면, 다른 py로 나누어 놔서 'from ~ import' 단계에서 무한 circle로 에러가 걸린다.
   - 즉, 'from ~ import' 단계부터 순환이 되면 안되게 설계해야한다. (밑으로 내려가지 않는다. 논리적으로 끝이 있다고 해도 진행 자체가 안 된다.)
   - 해결법 중 하나는 serializer class 안에 serailizer class를 넣는 것, 
   - 꼭 ModelSerializer이 아닌, 만들어 놓은 serializer class를 받아오는 방법이 있다.

3. 'ManyToManyField'는 M:N 관계에서 Foreign Key로 ~_id를 자동적으로 만들어줘서 굳이 변수를 만들어 할당할 필요 없다.
   - 생각보다도 더 편의성이 높은 tool

4. Git pull 받고 새로운 환경에서 시작할 때 자동적으로 해야할 것
   - 가상환경 설정 & 활성화
   - requirements.txt 다운 받기
   - makemigrations & migrate 하기
   - json data load 하기(반드시 model 정의 및 migrate 이후에 진행)

5. 홈페이지에서 할 수 있는 작업은 'GET' 밖에 없다!
   - 'POST', 'PULL', 'DELETE' 같은 작업은 Postman에서 진행해야 한다.

</br>

## 진행 상황
- 