<template>
  <div>
    <h1>만점~!</h1>
    <h1>당신은 영화 마스터</h1>
    <h1>개봉예정작들 추천해드릴게요! </h1>

    <div class="">
      <div class="">
        <img :src="imgUrl" alt="">
      </div>
    </div>
    <p>{{ randomMovie.title }}</p>
    <button @click="getRandomMovie" class="btn btn-warning d-grid gap-2 col-6 mx-auto">다른 영화</button>
  </div>
</template>

<script>
import lodash from 'lodash'
import axios from 'axios'

const IMG_URL = 'https://image.tmdb.org/t/p/w300'

export default {
  name: 'FourAnswerView',
  data () {
    return {
      moviesData: [],
      randomMovie: '',
      imgUrl: null,
      currentPage: 1,
    }
  },

  methods: {
    getRandomMovie () {
      if(lodash.isEmpty(this.moviesData)) {
        axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/movie/upcoming?api_key=db499efb2cc0ba6f9698b4699f1b762e&language=ko-KR&page=${this.currentPage}`
        })
        .then((response) => {
          this.moviesData = response.data.results
          this.currentPage = this.currentPage < 32 ? this.currentPage + 1 : 1
          this.randomMovie = lodash.sample(this.moviesData)
          this.imgUrl = `${IMG_URL}` + this.randomMovie.poster_path
        })
      } else {
        this.randomMovie = lodash.sample(this.moviesData)
        this.moviesData = this.moviesData.filter(movie => movie !== this.randomMovie)
        this.imgUrl = `${IMG_URL}` + this.randomMovie.poster_path
      }
    },
  },
  
  mounted() {
    this.getRandomMovie()
  },
}
</script>

<style>

</style>