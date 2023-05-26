<template>
  <div class="container">
    <b-row class="justify-content-md-center">
      <b-col md="6">
        <h1 class="text-center">Sign Up Page</h1>
        <b-form @submit.prevent="signUp">
          <b-form-group id="usernameGroup" label="Username" label-for="username">
            <b-form-input id="username" type="text" v-model="username" required placeholder="Username"></b-form-input>
          </b-form-group>
  
          <b-form-group id="password1Group" label="Password" label-for="password1">
            <b-form-input id="password1" type="password" v-model="password1" required placeholder="Password"></b-form-input>
          </b-form-group>

          <b-form-group id="password2Group" label="Password Confirmation" label-for="password2">
            <b-form-input id="password2" type="password" v-model="password2" required placeholder="Confirm Password"></b-form-input>
          </b-form-group>
  
          <b-button type="submit" variant="primary">SignUp</b-button>
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
const NOW_PLAYING_URL = `https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}&language=ko-KR`;

export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      randomMovie: '',
      imgUrl: null,
    }
  },
  created() {
    this.getRandomMovie()
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
    } ,
    getRandomMovie () {

      axios({
        method: 'get',
        url: NOW_PLAYING_URL
      })
      .then((response) => {
        const moviesData = response.data.results

        this.randomMovie = lodash.sample(moviesData)
        this.imgUrl = `${IMG_URL}` + this.randomMovie.poster_path
      })
    }
  }
}
</script>
