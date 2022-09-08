<template>
  <div>
    <h3>echart前后端交互使用</h3>
    <div id="main" :style="{width: '350px', height: '350px'}"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
export default {
  name: "testCharts",
  data() {
    return {
      labList: [],
      dayCnt: "0"
    }
  },
  mounted() {
    this.getCnt();
    this.initChart();
  },
  methods: {
    getCnt() {
      this.$axios.get('http://127.0.0.1:5000/getCnt',)
      .then((res) => {
        this.dayCnt = res.data.cnt
      });
    },
    initChart() {
      this.char = echarts.init(document.getElementById("main"));
      this.char.setOption({
        roseType: 'angle',
        tooltip: {},
        series: [
          {
            name: '访问来源',
            type: 'pie',
            radius: '55%',
            data: []
          }
        ]
      });
      
      this.$axios.get('http://127.0.0.1:5000/getInfo', {
        params: {
          cnt: this.dayCnt,
          flag: 2
        }
      })
        .then((res) => {
          console.log('访问后台');
          for (var key in res.data) {
            console.log(key)
          }
          // this.labList = res.data.data.dayInfo;
          // console.log(this.labList);
          //转成json
          // // this.labList = eval('('+data+')');
          // this.char.setOption({
          //   series: [
          //     {
          //       name: '访问来源',
          //       type: 'pie',
          //       radius: '55%',
          //       data: this.labList
          //     }
          //   ]
          // })
        });

    },
  }
}
</script>

