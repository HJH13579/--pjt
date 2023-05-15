<template>
  <div class="random-movie-list">
    <button @click="getRandomMovie" class="btn btn-success d-grid gap-2 col-6 mx-auto" >PICK</button>
    
    <br>
    <br>
    <img :src="imgUrl" alt="">
    <p>{{randomMovie.title}}</p>
  </div>
</template>


<script>
import lodash from 'lodash'
import axios from 'axios'



const TOP_RATED_URL =  `https://api.themoviedb.org/3/movie/top_rated?api_key=225d4451041ef2f3386801d92ef16935&language=ko-KR`
const IMG_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name: 'RandomView',
  data () {
    return {
      randomMovie: '',
      imgUrl: null,
    }
  },
  created() {
    this.getRandomMovie()
  },
  methods: {
    getRandomMovie () {

      axios({
        method: 'get',
        url: TOP_RATED_URL
      })
      .then((response) => {
        const moviesData = response.data.results

        this.randomMovie = lodash.sample(moviesData)
        this.imgUrl = `${IMG_URL}` + this.randomMovie.poster_path
      })
    }
  },
}
</script>


<style>

</style>