<template>
  <NavBar></NavBar>
  <router-view />
</template>

<script>
import NavBar from './components/NavBar.vue';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap"
import { getCurrentInstance } from "vue"

export default {
    components: { NavBar },
    setup() {
      getCurrentInstance()?.appContext.config.globalProperties.$axios.get('http://127.0.0.1:5000/getDayInfo')
      .then((res) => {
        dayInfo.value = res.data
      });
    }
}
</script>

<style>
body {
  background-image: url("@/assets/backpg.png");
  background-size: cover;
}
</style>
