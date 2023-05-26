<template>
  <div>
    <h1>영화이야기</h1>
    <b-card v-if="movie" title="Movie Details" class="mb-2 text-muted">
      <h4 class="mb-2">제목: {{ movie.title }}</h4>
      <h4 class="mb-2">줄거리: {{ movie.overview }}</h4>
      <h4 class="mb-2">개봉일: {{ movie.released_date }}</h4>
      <h4 class="mb-2">평점: {{ movie.vote_avg }}</h4>
      <img :src="imgUrl" alt="">
      <h4>예고편</h4>
      <YouTubeMovies/>
    </b-card>
    
    <b-card title="댓글 작성" class="mb-2">
      <form @submit.prevent="submitComment">
        <b-form-textarea v-model="commentContent" placeholder="댓글을 작성하세요..." rows="3"></b-form-textarea>
        <b-button type="submit" variant="primary">작성</b-button>
      </form>
    </b-card>
    <!-- 작성된 댓글들을 보여주는 곳 -->
    <b-card title="댓글 목록" class="mb-2 black">
    <div v-for="comment in comments" :key="comment.id">
      <b-card title="Comment" class="mb-2">
        <!-- <p class="mb-2">작성자: {{ comment.user.username }}</p>  -->
        <p class="mb-2">작성자: {{ comment.author_name }}</p>
        <!-- <p class="mb-2">작성자: {{ getRandomName() }}</p>  -->
        <p class="mb-2">내용: {{ comment.content }}</p>
        <p class="mb-2">작성일: {{ comment.created_at }}</p>
      </b-card> 
    </div>

    </b-card>
  </div>
</template>


<script>
import axios from 'axios';
import lodash from 'lodash'
import YouTubeMovies from '@/components/Movies/YouTubeMovies.vue'
const IMG_URL = 'https://image.tmdb.org/t/p/w300';

export default {
  components: {
    YouTubeMovies
  },
  data() {
    return {
      movie: null,
      commentContent: '',
      comments: [],
      statelists: ['일하는', '요구사항이 많은', '피곤한', '그만두고 싶은', '이직하고 싶은', '영화보기를 싫어하는', '말이 많은', '감기에 걸린', '출근하기 싫은', '주말이 기다려지는', '휴가 나온', '히오스를 좋아하는'],
      namelists: ['개발자', '프로', '아마추어', '감자', '유튜버', '복학생', '클라이언트', '영화광', '포켓몬 트레이너', '축구 선수', '프로게이머', '케이팝 아이돌'],
      randomname: '',
      randomstate: '',

    };
  },
  computed: {
    imgUrl() {
      return `${IMG_URL}${this.movie.poster_path}`;
    },
    combinedName () {
      return this.lodash.sample(this.statelists) + '' + this.lodash.sample(this.namelists)
    }
  },
  created() {
    const movieId = this.$route.params.id;
    axios.get(`http://localhost:8000/movies/${movieId}/`, 
    { headers: {
        'Authorization': `Token ${this.$store.state.token}`,}}
    )
      .then(response => {
        this.movie = response.data;
      })
      .catch(error => {
        console.log(error);
      });
    this.getComments()   // 페이지 로드 시 댓글 목록 불러옴  
  },
  methods: {
    getComments() {
      const movieId = this.$route.params.id;
      axios.get(`http://localhost:8000/movies/${movieId}/comments/`, { headers: {
        'Authorization': `Token ${this.$store.state.token}`,}})
        .then(response => {
          this.comments = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    submitComment() {
      const movieId = this.$route.params.id;
      const randomName = this.getRandomName();
      const payload = {
        movie_id: movieId,
        content: this.commentContent,
        movie: this.movie.movie_id, //이건 왜 중복 키값이 아니지? 
        user: 1, //id값 어떻게 pk로 줄 지 생각해보자...아무 수나 넣어도 되네
        author_name: randomName, //장고에 랜덤네임 저장
      };

      axios.post(`http://localhost:8000/movies/${movieId}/create_comment/`, payload, { headers: {
        'Authorization': `Token ${this.$store.state.token}`,}})
        .then(response => {
          console.log('댓글 작성 완료:', response.data);
          // 댓글 작성 성공 후 필요한 처리를 추가. 댓글 목록 불러오기 보여주기 등
          this.getComments()
        })
        .catch(error => {
          console.log('댓글 작성 에러:', error);
        });

      this.commentContent = ''; // 작성된 댓글 내용 초기화
    },
    getRandomName() {
      const randomState = lodash.sample(this.statelists);
      const randomName = lodash.sample(this.namelists);
      return randomState + ' ' + randomName;
    },

  },
};
</script>

<style>
.black {
  color: black;
}
</style>
