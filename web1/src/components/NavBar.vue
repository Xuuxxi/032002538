<!-- <template>
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
        </ul>
        <ul class="navbar-nav">
          <select class="nav-link bg-dark" aria-label="Default select example" name="select_list" @change="changeCnt($event.target.value)">
            <option class="nav-link" selected>请选择查询日期</option>
            <option class="nav-link" value="0">{{dayInfo[0]}}</option>
            <option class="nav-link" value="1">{{dayInfo[1]}}</option>
            <option class="nav-link" value="2">{{dayInfo[2]}}</option>
            <option class="nav-link" value="3">{{dayInfo[3]}}</option>
            <option class="nav-link" value="4">{{dayInfo[4]}}</option>
            <option class="nav-link" value="5">{{dayInfo[5]}}</option>
            <option class="nav-link" value="6">{{dayInfo[6]}}</option>
          </select>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { useRoute } from 'vue-router'
import { computed, ref } from 'vue'
import { getCurrentInstance } from "vue"
export default {
  setup() {
    const route = useRoute();
    let route_name = computed(() => route.name)
    let dayInfo = ref({})
    getCurrentInstance()?.appContext.config.globalProperties.$axios.get('http://127.0.0.1:5000/getDayInfo')
      .then((res) => {
        dayInfo.value = res.data
      });

    return {
      route_name,
      dayInfo
    }
  },
  methods: {
    changeCnt(val){
      this.$axios.get('http://127.0.0.1:5000/setCnt',{
        params: {
          cnt: val
        }
      })
      .then((res) => {
        console.log('改变选择日期');
        console.log(res.data);
      });
    }
  }
}
</script>

<style scoped>

</style> -->