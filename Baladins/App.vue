<script setup lang="ts">
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
</script>

<template>
  <Header></Header>
  <body>
    <RouterView></RouterView>
  </body>

  <Footer></Footer>
</template>

<style scoped>
html, body {
  margin: 0;
  padding: 0; 
  height: 100%;
  margin-bottom: 80px;
}

header {
  line-height: 1.5;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}

footer{
  position: absolute;
}



</style>
