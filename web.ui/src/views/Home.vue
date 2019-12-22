<template>
  <div class="home">
    <YouTubeLinkUI msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import YouTubeLinkUI from '@/components/YouTubeLinkUI.vue'

export default {
  name: 'home',
  components: {
    YouTubeLinkUI
  }
}
</script>
