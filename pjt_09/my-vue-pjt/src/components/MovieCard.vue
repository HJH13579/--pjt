<template>
  <div class>
    <img :src="imgUrl" alt="">
    <p>{{movie?.title}}</p>
    <p>{{movie?.overview}}</p>
  </div>
</template>

<script>
const IMG_URL = 'https://image.tmdb.org/t/p/w500'

export default {
  name: 'MovieCard',
  props:{
    movie : Object,
  },
  computed:{
    imgUrl(){
      // return '정해진 url http' + this.movie.{axios로 받아온 데이터의 url}
      return `${IMG_URL}` + this.movie.poster_path
    }
  },
}
</script>