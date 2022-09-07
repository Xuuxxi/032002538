<template>
  <NavBar></NavBar>
  <router-view />
</template>

<script>
import NavBar from './components/NavBar.vue';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap"
import $ from 'jquery';
import { ref } from 'vue';

export default {
  components: { NavBar },
  setup() {
    let data = ref([]);
    $.ajax({
      url: "http://127.0.0.1:5000/getInfo",
      data: {},
      type: "get",
      success(resp) {
        data = resp.data;
        console.log(data.value);
      },
      error(resp) {
        console.log(resp);
      }
    })

  }
}
</script>

<style>
body {
  background-image: url("@/assets/backpg.png");
  background-size: cover;
}
</style>
