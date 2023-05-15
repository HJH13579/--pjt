<template>
  <div class="article-list">
    <h1>WatchListForm</h1>
    <WatchListItem 
    v-for="article in articles" :key="article.id" :article="article"
    />
  </div>
</template>

<script>
import WatchListItem from '@/components/WatchListItem.vue'

export default {
  name: 'WatchListFrom',
  components: {
    WatchListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>

</style>