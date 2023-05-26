<template>
  <div>
    <h1>영잘알이시군요! 그렇다면 새로 나오는 영화들을 구경해보시는건 어때요?</h1>
    <UpcomingMovies/>
  </div>
</template>

<script>
import UpcomingMovies from '../Movies/UpcomingMovies.vue'

export default {
  name: 'SuccessQuizView',
  components: {
    UpcomingMovies,
  },

}
</script>

<style>

</style>