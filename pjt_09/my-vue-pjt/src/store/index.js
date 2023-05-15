import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articles: []
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    ADD_ARTICLES(state, article) {
      state.articles.push(article) 
    },
  },
  actions: {
    getArticles(context, articles) {
      context.commit('GET_ARTICLES', articles)
    },

  },
  modules: {
  }
})
