<template>
  <div>
    <div id="main" style="width:100%;height:700px;"></div>
  </div>
</template>

<script>
function makeOption(day_list) {
  return {
    dataset: [
      {
        dimensions: ['name', 'new_add'],
        source: [
          ['香港当日新增', day_list[0]],
          ['台湾当日新增', day_list[1]],
          ['澳门当日新增', day_list[2]],
        ]
      },
      {
        transform: {
          type: 'sort',
          config: { dimension: 'new_add', order: 'desc' }
        }
      }
    ],
    xAxis: {
      type: 'category',
      axisLabel: { interval: 0, rotate: 30 }
    },
    yAxis: {},
    series: {
      type: 'bar',
      encode: { x: 'name', y: 'new_add' },
      datasetIndex: 1
    }
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
        this.char = echarts.init(document.getElementById("main"));
        var dayInfo = res.data
        // 获取日期对应具体信息
        this.$http({
          method: "post",
          url: "http://localhost:8081/dayInfo/getInfo",
          data: {
            curTime: dayInfo
          }
        }).then((res) => {
          var cur_hk = res.data.hkTotal, cur_tw = res.data.twTotal, cur_am = res.data.amTotal
          this.$http({
            method: "get",
            url: "http://localhost:5000/sub",
            params: {
              curDay: dayInfo
            }
          }).then((res) => {
            this.$http({
              method: "post",
              url: "http://localhost:8081/dayInfo/getInfo",
              data: {
                curTime: res.data.cul_day
              }
            }).then((res) => {
              let data_list = new Array();
              data_list.push(parseInt(cur_hk) - parseInt(res.data.hkTotal))
              data_list.push(parseInt(cur_tw) - parseInt(res.data.twTotal))
              data_list.push(parseInt(cur_am) - parseInt(res.data.amTotal))

              this.char.setOption(makeOption(data_list));
            })
          })
        })
      });
    },
  }
}
</script>

