<template>
  <div>
    <h1>WatchListItem</h1>
    <p>{{ article.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
      article: Object,
  },
}
</script>

<style>

</style>