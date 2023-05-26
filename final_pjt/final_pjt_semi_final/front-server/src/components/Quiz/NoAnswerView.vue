<template>
  <div>
    <h1> 빵점~! </h1>
    <h1> 영화의 재미를 같이 찾아볼까요? </h1>
    <h1> 진짜 유명한 영화들 도전해보시겠어요? </h1>

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
  name: 'ThreeAnswerView',
  data () {
    return {
      moviesData: [],
      randomMovie: '',
      imgUrl: null,
    }
  },

  methods: {
    getRandomMovie () {
      if(lodash.isEmpty(this.moviesData)) {
        axios({
          method: 'get',
          url: 'http://localhost:8000/movies/',
          headers: {
            'Authorization': `Token ${this.$store.state.token}`,
          }
        })
        .then((response) => {
          this.moviesData = response.data.filter(movie => movie.popularity > 1200)
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