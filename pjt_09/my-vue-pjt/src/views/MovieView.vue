<template>
  <div class="top-rated-movie-list">
    <h1>MovieView</h1>
    <MovieCard 
      v-for="movie in movies" 
      :key="movie.id" 
      
      :movie="movie"
    />
  </div>
</template>

<script>
import axios from 'axios'
const TOP_RATED_URL =  `https://api.themoviedb.org/3/movie/top_rated?api_key=db499efb2cc0ba6f9698b4699f1b762e&language=ko-KR&page=1`

import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieView',
  components: {
    MovieCard,
  },
  data () {
    return {
      movies: null,
    }
  },
  created() {
    this.getTopRatedMovies()
  },
  methods: {
    getTopRatedMovies () {
      axios({
        method: 'get',
        url: TOP_RATED_URL
      })
      .then((response) => {
        const moviesData = response.data.results
        this.movies = moviesData 
      })
    }
  }
}
</script>

<style>

</style>