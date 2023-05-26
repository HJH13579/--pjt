<template>
  <div>
    <h1>HOME</h1>
    <!-- <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link> -->
    <h3>찾으시는 사이트가 있으신가요?</h3>
    <img height="60%" :src="seaImage" alt="Sea Image" id="bgimage">
    <h4 class="left-align">어디서 볼까?</h4>
    <a target="_blank" href="https://www.netflix.com/kr/">
       <img class="resized" src="@/assets/넷플릭스.png" alt="넷플릭스 로고">
    </a>
    <a target="_blank" href="https://watcha.com/">
       <img class="resized" src="@/assets/왓챠.jpg" alt="왓챠 로고">
    </a>
    <a target="_blank" href="https://www.disneyplus.com/ko-kr?cid=DSS-Search-Google-71700000088339394-&s_kwcid=AL!8468!3!620347232144!e!!g!!%EB%94%94%EC%A6%88%EB%8B%88%20%ED%94%8C%EB%9F%AC%EC%8A%A4&gclid=CjwKCAjw67ajBhAVEiwA2g_jEKblX1EgEYqJ6Wt9RurkYuLRXJYGDyAQfWEx2F982dNyKekn_ahSExoCVHwQAvD_BwE&gclsrc=aw.ds">
       <img class="resized" src="@/assets/디즈니.jpg" alt="디즈니 로고">
    </a>
    <a target="_blank" href="https://www.apple.com/kr/apple-tv-plus/">
       <img class="resized" src="@/assets/애플티비.png" alt="애플티비 로고">
    </a>
    <hr>
    <h4 class="left-align">평론/정보</h4>
    <a target="_blank" href="https://www.kofic.or.kr/kofic/business/main/main.do">
      <img class="resized" src="@/assets/영진위.jpg" alt="영화진흥위원회 로고">
    </a>
    <a target="_blank" href="http://www.cine21.com/misc/doc/sitemap">
       <img class="resized" src="@/assets/씨네21.jpg" alt="씨네21 로고">
    </a>
    <a target="_blank" href="https://www.rottentomatoes.com/">
       <img class="resized" src="@/assets/로튼토마토.png" alt="로튼토마토 로고">
    </a>
    <a target="_blank" href="https://www.themoviedb.org/?language=ko-KR">
       <img class="resized" src="@/assets/tmdb.png" alt="tmdb 로고">
    </a>
     <a target="_blank" href="https://www.metacritic.com/">
       <img class="resized" src="@/assets/메타크리틱.jpg" alt="메타크리틱 로고">
    </a>
    <a target="_blank" href="https://www.imdb.com/">
       <img class="resized" src="@/assets/imdb.png" alt="imdb 로고">
    </a>
    <hr>
    <h4 class="left-align">영화관에 가볼까?</h4>
    <a target="_blank" href="http://www.cgv.co.kr/ticket/">
      <img class="resized" src="@/assets/cgv.png" alt="cgv 로고">
    </a>
    <a target="_blank" href="https://www.megabox.co.kr/booking">
       <img class="resized" src="@/assets/메가박스.png" alt="메가박스 로고">
    </a>
    <a target="_blank" href="https://www.lottecinema.co.kr/NLCHS/Ticketing">
       <img class="resized" src="@/assets/롯데시네마.png" alt="롯데시네마 로고">
    </a>
   
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
   
  },
  methods: {
   
  },
  data() {
    return {
      seaImage: require('@/assets/sea.png')
    }
  }
}
</script>

<style>
.resized {
  width: 200px;  /* 원하는 너비로 변경 */
  height: auto;  /* 높이를 auto로 설정하여 원본 이미지의 비율을 유지 */
}
.left-align {
  text-align: left;
}
</style>
