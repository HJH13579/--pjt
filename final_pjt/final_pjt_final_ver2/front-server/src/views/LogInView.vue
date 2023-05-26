<template>
  <div class="container">
    <b-row class="justify-content-md-center">
      <b-col md="6">
        <h1 class="text-center">LogIn Page</h1>
        <b-form @submit.prevent="login">
          <b-form-group id="usernameGroup" label="Username" label-for="username">
            <b-form-input id="username" type="text" v-model="username" required placeholder="Username"></b-form-input>
          </b-form-group>
  
          <b-form-group id="passwordGroup" label="Password" label-for="password">
            <b-form-input id="password" type="password" v-model="password" required placeholder="Password"></b-form-input>
          </b-form-group>
  
          <b-button type="submit" variant="primary">LogIn</b-button>
        </b-form>
      </b-col>
    </b-row>
    <img :src="imgUrl" alt="">
    <p>{{randomMovie.title}}</p>
  </div>
</template>

<script>
import lodash from 'lodash'
import axios from 'axios'


const IMG_URL = 'https://image.tmdb.org/t/p/w500'
const API_KEY = 'db499efb2cc0ba6f9698b4699f1b762e';
const POPULAR_URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}&language=ko-KR&page=1`
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      randomMovie: '',
      imgUrl: null,
    }
  },
    created() {
    this.getRandomMovie()
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, 
        password
      }

      this.$store.dispatch('login', payload)
      
    },
    getRandomMovie () {

      axios({
        method: 'get',
        url: POPULAR_URL
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
