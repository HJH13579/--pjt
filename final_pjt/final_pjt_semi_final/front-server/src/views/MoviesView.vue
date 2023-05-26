<template>
  <div class="scroll-container">
    <b-card title="환영합니다" class="mb-2 text-muted">
      <h1 class="mb-2">퀴즈를 풀고 나에게 맞는 영화를 추천받으세요!</h1>
    </b-card>
    <h4>현재상영작</h4>
    <NowPlayingMovies/>
    <h4>평점 높은 영화</h4>
    <TopRatedMovies/>
    <h4>유명한 영화</h4>
    <PopularMovies/>
    <h4>개봉예정작</h4>
    <UpcomingMovies/>
    
  </div>
</template>

<script>
import NowPlayingMovies from '../components/Movies/NowPlayingMovies.vue'
import TopRatedMovies from '../components/Movies/TopRatedMovies.vue'
import PopularMovies from '../components/Movies/PopularMovies.vue'
import UpcomingMovies from '../components/Movies/UpcomingMovies.vue'

export default {
  name: 'MoviesView',
  components: {
    NowPlayingMovies,
    TopRatedMovies,
    PopularMovies,
    UpcomingMovies,
  },
}
</script>

<style>

</style>