import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    token: null,
    profile: {}
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
     // 프로필 정보 반환
    profile(state) {
      return state.profile
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    // signup & login -> 완료하면 토큰 발급
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'ArticleView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    // 로그아웃 관련된 내용
    DELETE_TOKEN(state){
      state.token = null
      location.reload()
    },
    // 프로필 관련 내용
    SET_PROFILE(state, profile) {
      state.profile = profile
    },
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res) => {
        // console.log(res, context)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        alert('회원가입이 완료되었습니다!')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        alert('성공적으로 로그인되었습니다!')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout(){
      this.commit("DELETE_TOKEN")
      // commit("DELETE_TOKEN") 로그아웃 구현입니다.
      alert('성공적으로 로그아웃되었습니다!')
    },
    // 프로필 구현
    getProfile(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((response) => {
        context.commit('SET_PROFILE', response.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
