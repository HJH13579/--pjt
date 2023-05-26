<template>
  <div class="container mt-3">
    <div class="row">
      <carousel :perPage="7" :navigationEnabled="true" :paginationEnabled="false" :loop="true" :autoplay="true" :autoplaySpeed="5000">
        <slide v-for="movie in movies" :key="movie.id">
          <div class="card mb-2">
            <router-link :to="`/movie/${movie.id}`">
              <img class="card-img-top" :src="getImgUrl(movie)" alt="Movie Poster">
            </router-link>
          </div>
        </slide>
      </carousel>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Carousel, Slide } from 'vue-carousel';

const API_KEY = 'db499efb2cc0ba6f9698b4699f1b762e';
const NOW_PLAYING_URL = `https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}&language=ko-KR`;

export default {
  name: 'MoviesView',
  components: {
    Carousel,
    Slide,
  },
  data() {
    return {
      movies: [],
    };
  },
  created() {
    this.getNowPlayingMovies()
  },
  methods: {
    getNowPlayingMovies() {
      axios({
        method: 'get',
        url: NOW_PLAYING_URL,
      })
        .then((response) => {
          const moviesData = response.data.results;
          this.movies = moviesData;
        });
    },
    getImgUrl(movie) {
      const baseImgUrl = 'https://image.tmdb.org/t/p/w200';
      return baseImgUrl + movie.poster_path;
    },
  },
};
</script>

<style>
.card-img-top {
  height: 100%;
  width: 100%;
  object-fit: cover;
}
.card-img-top {
  height: 100%;
  width: 100%;
  object-fit: cover;
}
.VueCarousel-navigation-button,
.VueCarousel-navigation-next,
.VueCarousel-navigation-prev {
  color: red !important;
}

.VueCarousel-navigation-next:hover,
.VueCarousel-navigation-prev:hover {
  color: darkred
}
/* .hover-zoom {
  transition: transform 0.3s ease-in-out;
}

.hover-zoom:hover {
  transform: scale(1.4);
} */

</style>