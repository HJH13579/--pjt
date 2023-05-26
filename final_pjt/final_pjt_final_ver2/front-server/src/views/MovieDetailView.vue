<template>
  <div>
    <b-card title="Movie Details" class="mb-2 text-muted">
      <h4 class="mb-2">제목 : {{ movie?.title }}</h4>
      <h4 class="mb-2">줄거리 : {{ movie?.overview }}</h4>
      <h4 class="mb-2">개봉일 : {{ movie?.release_date }}</h4>
      <h4 class="mb-2">평점 : {{ movie?.vote_average }}</h4>
      <h4 class="mb-2">관람평 수 : {{ movie?.vote_count }}</h4>
      <h4 class="mb-2">장르 : {{ movie?.genres }}</h4>
      <h4 class="mb-2">런타임 : {{ movie?.runtime }}</h4>
    </b-card>

  <div>
    <button variant="primary" @click="likePost">
      {{ liked ? 'Unlike' : 'Like' }} Post
    </button>
    <p>Total Likes: {{ totalLikes }}</p>
  </div>

  </div>
</template>

<script>
import axios from 'axios'

const API_KEY = 'db499efb2cc0ba6f9698b4699f1b762e'

export default {
  data() {
    return {
      movie: null,
      liked: false,
      totalLikes: 0,
      postId: this.$route.params.id,
    };
  },
  created() {
    this.getMovieDetail()
    
  },
  methods: {
    getMovieDetail() {
      const id = this.$route.params.id
      const DETAIL_URL = `https://api.themoviedb.org/3/movie/${id}?api_key=${API_KEY}&language=ko-KR`
      
      axios({
        method: 'get',
        url: DETAIL_URL
      })
      .then((response) => {
        this.movie = response.data
      })
    },
 
    likePost() {
    this.liked = !this.liked
    this.totalLikes = this.liked ? this.totalLikes + 1 : this.totalLikes - 1
    },
    
  }
}
</script>