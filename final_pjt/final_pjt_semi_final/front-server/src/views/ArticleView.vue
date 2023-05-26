<template>
  <div>
    <h1>HOME</h1>
    <img height="60%" :src="seaImage" alt="Sea Image" id="bgimage">
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleView',
  components: {
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      // if (this.isLogin) {
      //   this.$store.dispatch('getArticles') }
      // } else {
      //   alert('로그인이 필요한 페이지입니다...')
      //   this.$router.push({ name: 'LogInView' })
      // }

      // 로그인이 되어 있으면 getArticles action 실행
      // 로그인 X라면 login 페이지로 이동
    }
  },
  data() {
    return {
      seaImage: require('@/assets/sea.png')
    }
  }
}
</script>

<style>

</style>
