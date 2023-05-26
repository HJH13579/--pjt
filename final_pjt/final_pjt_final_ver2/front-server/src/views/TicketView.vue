<template>
  <div class="container">
   <svg width="0" height="0">
  <defs>
   <clipPath id="ticket-clip">
      <path d="M0,19 L13,0 L26,19 L39,0 L52,19 L65,0 L78,19 L91,0 L104,19 L117,0 L130,19 L143,0 L156,19 L169,0 L182,19 L195,0 L208,19 L221,0 L234,19 L247,0 L260,19 L260,361 L247,380 L234,361 L221,380 L208,361 L195,380 L182,361 L169,380 L156,361 L143,380 L130,361 L117,380 L104,361 L91,380 L78,361 L65,380 L52,361 L39,380 L26,361 L13,380 L0,361 Z" />
    </clipPath>
  </defs>
</svg>
    
    <button @click="getRandomMovie" class="btn btn-warning d-grid gap-2 col-6 mx-auto">뽑기</button>
    <br>
    <br>
    <div class="ticket">
      <div class="center">
        <img :src="imgUrl" alt="" style="clip-path: url(#ticket-clip);">
      </div>
    </div>
    <p>{{randomMovie.title}}</p>
  </div>
</template>

<script>
import lodash from 'lodash'
import axios from 'axios'
const TOP_RATED_URL =  `https://api.themoviedb.org/3/movie/top_rated?api_key=db499efb2cc0ba6f9698b4699f1b762e&language=ko-KR&page=1`
const IMG_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name: 'TicketView',
  data () {
    return {
      randomMovie: '',
      imgUrl: null,
    }
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
    },
  }
}
</script>

<style scoped>
.ticket {
  width: 260px;
  height: 350px;
  background-image: imgUrl;
  background-size: cover;
  background-position: center;
  position: relative;
  overflow: hidden;
}



.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh; /* 조정 가능한 높이 값 */
}

.center {
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>