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
            <router-link :class="route_name == 'nation_info' ? 'nav-link active' : 'nav-link'"
              :to="{name:'nation_info'}">全国信息
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :class="route_name == 'pro_info' ? 'nav-link active' : 'nav-link'" :to="{name:'pro_info'}">
              各省份信息
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :class="route_name == 'else_info' ? 'nav-link active' : 'nav-link'" :to="{name:'else_info'}">
              港澳台信息
            </router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              截至当前接种疫苗：{{medNum}}(单位：万剂)
            </a>
          </li>
        </ul>
        <ul class="navbar-nav">
          <div class="input-group input-group-sm">
            <button class="input-group-text" @click="changeDay()">查询日期</button>
            <input type="text" class="form-control" aria-label="Sizing example input"
              aria-describedby="inputGroup-sizing-sm" placeholder="edit me" v-model="dayInfo">
            <button class="input-group-text" @click="myRed()">卫健委LINK</button>
          </div>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { useRoute } from 'vue-router'
import { computed } from 'vue'
//import { getCurrentInstance } from "vue"

export default {
  setup() {
    const route = useRoute();
    let route_name = computed(() => route.name)
    // let dayInfo = ref("")
    // let medNum = ref("")

    // getCurrentInstance()?.appContext.config.globalProperties.$axios.get('http://localhost:8081/curDay/getCurDay')
    //   .then((res) => {
    //     dayInfo.value = res.data

    //     $http('http://localhost:8081/urlInfo/getInfo', {
    //       method: "post",
    //       data: {
    //         url: dayInfo.value,
    //       }
    //     }).then((res) => {
    //       console.log(res.data)
    //       medNum.value = res.data.curTime
    //       console.log(medNum.value)
    //     });
    //   });

    return {
      route_name,
    }
  },
  data() {
    return {
      dayInfo: "",
      medNum: "",
      wjw_link: ""
    }
  },
  mounted() {
    this.getDay()
  },
  methods: {
    myRed() {
      alert("即将跳转到中华人民共和国国家卫生健康委员会对应日期的疫情信息界面！")
      window.location.replace(this.wjw_link)
    },
    getDay() {
      this.$http.get('http://localhost:8081/curDay/getCurDay')
        .then((res) => {
          this.dayInfo = res.data

          this.$http('http://localhost:8081/urlInfo/getInfo', {
            method: "post",
            data: {
              url: this.dayInfo,
            }
          }).then((res) => {
            this.medNum = res.data.curTime
          });

          this.$http('http://localhost:8081/urlInfo/getInfo', {
            method: "post",
            data: {
              curTime: this.dayInfo,
            }
          }).then((res) => {
            this.wjw_link = res.data.url
          });
        });
    },
    changeDay() {
      var r = /[0-9]{4}-[0-1][0-9]-[0-3][0-9]/;
      if (r.test(this.dayInfo) == false) {
        alert("输入日期格式: yyyy-MM-dd !");
        return;
      }

      this.$http({
        method: "put",
        url: "http://localhost:8081/curDay/updCurDay",
        data: {
          curTime: this.dayInfo
        }
      }).then((res) => {
        this.dayInfo = res.data
        location.reload()
      });
    }
  }
}
</script>

<style scoped>

</style>