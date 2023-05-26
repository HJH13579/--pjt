import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import MoviesView from '@/views/MoviesView'
import MovieDetailView from '@/views/MovieDetailView'
import QuizView from '@/views/QuizView'
import RecommendView from '@/views/RecommendView'
import TicketView from '@/views/TicketView'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import FourAnswerView from '@/components/Quiz/FourAnswerView.vue'
import ThreeAnswerView from '@/components/Quiz/ThreeAnswerView.vue'
import TwoAnswerView from '@/components/Quiz/TwoAnswerView.vue'
import OneAnswerView from '@/components/Quiz/OneAnswerView.vue'
import NoAnswerView from '@/components/Quiz/NoAnswerView.vue'
import RecommendDetailView  from '@/components/Movies/RecommendDetailView.vue'
import ProfileView from '@/views/ProfileView'
import YouTubeMovies from '@/components/Movies/YouTubeMovies.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'ArticleView',
    component: ArticleView
  },

  {
    path: '/movies',
    name: 'MoviesView',
    component: MoviesView
  },

  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView 
  },
 
  {
    path: '/quiz',
    name: 'QuizView',
    component: QuizView
  },
 
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },

  {
    path: '/ticket',
    name: 'TicketView',
    component: TicketView
  },


  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  // 게시글 id
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
  // 퀴즈 결과에 따른 라우터
  {
    path: '/fouranswer',
    name: 'FourAnswerView',
    component: FourAnswerView,
  },

  {
    path: '/threeanswer',
    name: 'ThreeAnswerView',
    component: ThreeAnswerView,
  },

  {
    path: '/twoanswer',
    name: 'TwoAnswerView',
    component: TwoAnswerView,
  },

  {
    path: '/oneanswer',
    name: 'OneAnswerView',
    component: OneAnswerView,
  },

  {
    path: '/noanswer',
    name: 'NoAnswerView',
    component: NoAnswerView,
  },
  // 추천 페이지 개별 영화 이동
  {
    path: '/recommend/:id',
    name: 'RecommendDetailView',
    component: RecommendDetailView 
  },
    // 프로필
  {
    path: '/profile/',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/youtube/',
    name: 'YouTubeMovies',
    component: YouTubeMovies
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router