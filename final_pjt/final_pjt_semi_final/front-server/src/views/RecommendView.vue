<template>
  <div>
    <h1>Recommend Page</h1>
    <hr>
    <div class="movie-list">
      <router-link v-for="movie in movies" :key="movie.id" :to="`/recommend/${movie.id}`">
        <div class="movie-item">
          <h4>{{ movie.title }}</h4>
          <div class="image-container">
            <img :src="getImageUrl(movie.poster_path)" alt="Movie Poster" @mouseover="zoomInImage" @mouseout="zoomOutImage">
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const IMG_BASE_URL = 'https://image.tmdb.org/t/p/'; // 이미지 기본 URL
const IMG_SIZE = 'w200'; // 이미지 크기
export default {
  data() {
    return {
      movies: [],
    };
  },
  methods: {
    getImageUrl(posterPath) {
      if (posterPath) {
        return `${IMG_BASE_URL}${IMG_SIZE}${posterPath}`;
      }
      // 포스터 이미지가 없을 경우 기본 이미지 URL 반환하거나, 다른 처리를 할 수 있습니다.
      return 'default_image_url.jpg';
    },
    zoomInImage(event) {
      event.target.style.transform = 'scale(1.1)'; // 이미지를 1.1배 확대
    },
    zoomOutImage(event) {
      event.target.style.transform = 'scale(1)'; // 이미지를 원래 크기로 되돌림
    },
  },

  // headers에 인증과정 추가
  created() {
    axios.get('http://localhost:8000/movies/', {
       headers: {
        'Authorization': `Token ${this.$store.state.token}`,}
    })
      .then(response => {
        this.movies = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
};
</script>

<style>
.movie-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.movie-item {
  width: 200px;
  margin-bottom: 20px;
}

.image-container {
  overflow: hidden;
  transition: transform 0.5s ease-in-out;
}
</style>
