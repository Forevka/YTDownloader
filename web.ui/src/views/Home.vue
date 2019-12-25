<template>
  <div class="home">
    <LinkCollection/>
  </div>
</template>

<script>
// @ is an alias to /src
import LinkCollection from '@/components/LinkCollection.vue'

export default {
  name: 'home',
  components: {
    LinkCollection
  }
}
</script>
