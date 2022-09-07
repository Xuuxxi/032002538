<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <router-link class="navbar-brand" :to="{name:'home'}">疫情信息一览</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
        aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link :class="route_name == 'nation_info' ? 'nav-link active' : 'nav-link'" :to="{name:'nation_info'}">全国信息
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :class="route_name == 'pro_info' ? 'nav-link active' : 'nav-link'" :to="{name:'pro_info'}">各省份信息
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :class="route_name == 'else_info' ? 'nav-link active' : 'nav-link'" :to="{name:'else_info'}">港澳台信息
            </router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button"
              data-bs-toggle="dropdown" aria-expanded="false">
              Xuuxxi
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="#">假的个人中心</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">假的退出</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  import { useRoute } from 'vue-router'
  import { computed } from 'vue'
  export default {
    setup(){
      const route = useRoute();
      let route_name = computed(() => route.name)
  
      return{
        route_name
      }
    } 
  }
  </script>

<style scoped>

</style>