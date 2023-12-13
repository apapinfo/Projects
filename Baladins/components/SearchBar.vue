<template>
  <div>
    <input v-model="searchText" type="text" placeholder="Rechercher..." class="searchbar" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchText: ''
    }
  },
  methods: {
    search() {
      this.$emit('search', this.searchText)
    },
    filter() {
      this.$emit('filter')
    }
  }
}
</script>

<style>
.searchbar {
  width: 200px;
  top: 120px;
  left: 50%;
  background-color: #f8f6f6;
  color: #000000;
  padding: 10px;
  border-radius: 5px;
  opacity: 0.8;
}

</style>
