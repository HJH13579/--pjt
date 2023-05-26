<template>
  <div>
    <h1>{{ profile?.username }}</h1>
    <p>{{ profile?.id }}</p>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  created() {
    this.getProfile()
  },
  computed: {
    ...mapGetters([
      'profile',
    ])
  },
  methods: {
    ...mapActions([
      'getProfile'
    ])
  },
}
</script>

<style scoped>
/* 여기에 스타일을 추가하세요 */
</style>
