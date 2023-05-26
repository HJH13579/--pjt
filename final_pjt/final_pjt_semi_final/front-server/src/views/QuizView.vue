<template>
  <div class="quiz-container">
    <h1>영화 퀴즈</h1>
    <div v-if="!quizStarted">
      <button @click="startQuiz" class="btn btn-primary">퀴즈 시작</button>
    </div>
    <div v-else>
      <h2>{{ currentQuestion.question }}</h2>
      <div class="quizposter-container">
        <!-- <div class="quizposter" :style="`background-image: url('${imgUrl}')`"> -->
          <!-- <img :src="imgUrl" alt=""> -->
        <div
          v-for="(row, i) in rows"
          :key="i"
          class="row"
        >
          <div
            v-for="(col, j) in cols"
            :key="j"
            class="block"
            :style="{ 
              backgroundImage: `url('${imgUrl}')`,
              backgroundPosition: `-${j * 15}px -${i * 20}px`,
              visibility: (i + j) % 2 === 0 ? 'visible' : 'hidden'
            }"
          ></div>
        </div>
        <!-- </div> -->
      </div>
      <ul>
        <li v-for="(option, index) in currentQuestion.options" :key="index">
          <label>
            <input type="radio" :value="option" v-model="selectedAnswer">{{ option }}
          </label>
        </li>
      </ul>
      <button @click="submitAnswer" class="btn btn-primary">제출</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import lodash from 'lodash'

const API_KEY = 'db499efb2cc0ba6f9698b4699f1b762e'
const urls = [
  `https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}&language=ko-KR`,
  `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}&language=ko-KR&`,
  `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR`,
  `https://api.themoviedb.org/3/movie/upcoming?api_key=${API_KEY}&language=ko-KR`
]
const IMG_URL = 'https://image.tmdb.org/t/p/w300'

export default {
  name: 'QuizView',
  data() {
    return {
      quizStarted: false,
      randomMovie: null,
      imgUrl: null,
      questions: [
        {
          question: '이 영화의 제목은 무엇일까요?',
          options: null,
          answer: null,
        },
      ],
      currentQuestionIndex: 0,
      selectedAnswer: null,
      correctAnswersCount: 0,
      round: 0,

      // 구역 나누기
      rows: Array.from({ length: 15 }),  // 300px / 20px = 15
      cols: Array.from({ length: 20 }),  // 400px / 20px = 20
      // randomRow: Math.floor(Math.random() * 15),
      // randomCol: Math.floor(Math.random() * 20),
    };
  },
  created() {
    this.fetchRandomMovie()
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex]
    }
  },
  methods: {
    startQuiz() {
      // axios => 장고의 퀴즈 db를 건들여서 퀴즈를 가져와야 함
      this.quizStarted = true;
    },
    fetchRandomMovie () {
      const randomUrl = lodash.sample(urls)

      axios({
        method: 'get',
        url: randomUrl,
      })
      .then((response) => {
        const moviesData = response.data.results

        this.randomMovie = lodash.sample(moviesData)
        this.imgUrl = `${IMG_URL}` + this.randomMovie.poster_path 
        
        // 영화 제목을 첫 번째 질문의 정답으로 설정
        this.questions[0].answer = this.randomMovie.title

        // 옵션을 설정합니다. 먼저 정답을 배열에 추가합니다.
        let options = [this.randomMovie.title]
    
        // 나머지 3개의 옵션을 영화 목록에서 무작위로 선택하고, 정답과 다른 영화를 선택합니다.
        while(options.length < 4) {
          let movieOption = lodash.sample(moviesData)
      
          // 선택한 영화의 제목이 이미 옵션에 없는 경우에만 추가합니다.
          if(!options.includes(movieOption.title)) {
            options.push(movieOption.title)
          }
        }

        // 옵션을 무작위로 배열합니다.
        this.questions[0].options = lodash.shuffle(options)
      })
    },
    submitAnswer() {
      if (this.selectedAnswer === this.currentQuestion.answer) {
        this.correctAnswersCount++;
      }
      
      this.currentQuestionIndex++;
      this.selectedAnswer = null;
      
      // 현재 퀴즈를 모두 진행했는지 확인
      if (this.currentQuestionIndex === this.questions.length) {
        this.round++  // 한 라운드를 완료했으니 round 증가

        if (this.round < 4) {
          // 4 라운드 미만인 경우, 퀴즈 다시 시작
          this.currentQuestionIndex = 0
          this.selectedAnswer = null
          this.fetchRandomMovie()
          this.startQuiz()
        } else {
          // 4 라운드 모두 완료 경우, 결과 페이지로 이동
          this.navigateToResult()
        }
      }
    },
    navigateToResult() {
      if (this.correctAnswersCount === 4) {
        // 4문제 정답인 경우 다른 라우터로 이동 
        this.$router.push({name: 'FourAnswerView'})
      } else if (this.correctAnswersCount === 3) {
        // 3문제 정답인 경우 다른 라우터로 이동 
        this.$router.push({name: 'ThreeAnswerView'})
      } else if (this.correctAnswersCount === 2) {
        // 2문제 정답인 경우 다른 라우터로 이동
        this.$router.push({name: 'TwoAnswerView'})
      } else if (this.correctAnswersCount === 1) {
        // 1문제 정답인 경우 다른 라우터로 이동
        this.$router.push({name: 'OneAnswerView'})
      } else {
        // 0문제 정답인 경우 다른 라우터로 이동
        this.$router.push({name: 'NoAnswerView'})
      }
    }
  }
};
</script>

<style scoped>
ul {
    list-style: none;
}

.quiz-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  align-items: center;
}

.quizposter-container {
  /* width: 300px;
  height: 400px; */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.row {
  display: flex;
  width: 100%;
}

.block {
  width: 20px;
  height: 20px;
  /* background-size: 6000% 2000%;  300 * 20 = 6000, 400 * 5 = 2000 */
}
</style>