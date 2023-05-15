<template>
  <div>
    <h1>보고싶은 영화</h1>
    <form @submit.prevent="createArticle">
      <input type="text" id="title" v-model.trim="title">
      <input type="submit" value="Add" id="submit">
    </form>
    <WatchListForm />
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm.vue'

export default {
  name: 'WatchListView',
  components: {
    WatchListForm,
  },
  data() {
    return {
      title: '',
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    
  }
}
</script>

<style>

</style>