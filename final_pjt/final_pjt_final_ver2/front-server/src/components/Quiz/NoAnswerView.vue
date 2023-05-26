<template>
  <div>
    <h1>영화를 잘 안보시는군요... 그렇다면 유명한 명작들은 어떤가요?</h1>
    <PopularMovies/>
  </div>
</template>

<script>
import PopularMovies from '../Movies/PopularMovies.vue'

export default {
  name: 'FailureQuizView',
  components: {
    PopularMovies,
  },

}
</script>

<style>

</style>