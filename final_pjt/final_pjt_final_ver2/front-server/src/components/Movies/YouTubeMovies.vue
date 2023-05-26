<template>
  <div>
    <h1>YouTube 영상</h1>
    <!-- YouTube URL이 있을 경우 iFrame을 통해 영상 보여주기 -->
    <iframe v-if="youtubeUrl" width="560" height="315" :src="youtubeUrl" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</template>

<script>
import axios from 'axios';

const API_KEY = 'db499efb2cc0ba6f9698b4699f1b762e';

export default {
  name: 'YouTubeMovies',
  // props: ['movieId'],
  data() {
    return {
      trailerId: ''
    };
  },
  computed: {
    youtubeUrl() {
      if (this.trailerId) {
        // YouTube embed URL 사용
        return `https://www.youtube.com/embed/${this.trailerId}`;
      } else {
        return '';
      }
    }
  },
  methods: {
    async fetchTrailerId() {
      const movieId = this.$route.params.id
      const movieUrl = `https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${API_KEY}`;
  
      try {
        const response = await axios.get(movieUrl);
        const results = response.data.results;
        if (results.length > 0) {
          this.trailerId = results[0].key;
        }
      } catch (error) {
        console.log(error);
      }
    }
  },
  created() {
    this.fetchTrailerId();
  }
};
</script>

<style>
</style>
