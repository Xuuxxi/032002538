<template>
  <div>
    <div id="main" style="width:100%;height:700px;"></div>
  </div>
</template>

<script>
function makeOption(pro_add, pro_null,) {
  console.log(pro_add,pro_null);
  return {
    //option
  };
}

import * as echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
export default {
  name: "testChats",
  data() {
    return {
      labList: []
    }
  },
  mounted() {
    this.initDayInfo();
  },
  methods: {
    initDayInfo() {
      // 获取日期信息
      this.$http({
        method: "get",
        url: "http://localhost:8081/curDay/getCurDay",
      }).then((res) => {
        this.initChart(res.data)
      });
    },
    initChart(dayInfo) {
      this.char = echarts.init(document.getElementById("main"));

      // 获取日期对应具体信息
      this.$http({
        method: "post",
        url: "http://localhost:8081/dayInfo/getInfo",
        data: {
          curTime: dayInfo
        }
      }).then((res) => {
        let pro_add = res.data.proAdd
        let pro_null = res.data.proNull

        if (pro_add == '{}' || pro_add == '0' || pro_null == '{}' || pro_null == '0') {
          alert("该天数据未公示！（来源：国家卫生健康委员会）")
          return
        }

        this.char.setOption(makeOption(pro_add, pro_null));
      })
    },
  }
}
</script>

