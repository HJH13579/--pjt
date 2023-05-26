<template>
  <b-container id="app" class="background">
    <b-navbar id="navbar" toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand :to="{ name: 'ArticleView' }">MOON</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'ArticleView' }">Home</b-nav-item>
          <b-nav-item :to="{ name: 'MoviesView' }">영화</b-nav-item>
          <b-nav-item :to="{ name: 'QuizView' }">Quiz</b-nav-item>
          <b-nav-item :to="{ name: 'RecommendView' }">영화 게시판</b-nav-item>
          <b-nav-item :to="{ name: 'TicketView' }">오리지널 티켓 뽑기</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-if="!isLogin" :to="{ name: 'SignUpView' }">회원가입</b-nav-item>
          <b-nav-item v-if="!isLogin" :to="{ name: 'LogInView' }">로그인</b-nav-item>
          <b-nav-item v-if="isLogin" :to="{ name: 'ProfileView' }">프로필</b-nav-item>
          <b-button v-if="isLogin" type="button" class="logoutButton" @click="logout">LogOut</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <router-view/>

  </b-container>
</template>

<script>

export default {
  methods: {
    logout() {
      this.$store.dispatch("logout") // 로그아웃
    },
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부 확인
    }
  },
};
</script>

<style>

#app {
  font-family: 'Jua', sans-serif;
  min-height: 1000px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
}

#navbar {
  padding: 30px;
  font-family: 'Jua', sans-serif;
}

#navbar .nav-link {
  font-weight: bold;
  color: #9caab8;
}

#navbar .nav-link.router-link-exact-active {
  color: #42b983;
}

#image{
  width: max-content
}

img {
  max-width: 100%;
  height: auto;
}

</style>
