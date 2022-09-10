<template>
  <div>
    <div id="main" style="width:100%;height:700px;"></div>
  </div>
</template>

<script>

function makeOption(pro_add, pro_null) {
  return {
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    toolbox: {
      show: true,
      feature: {
        mark: { show: true },
        dataView: { show: true, readOnly: false },
        restore: { show: true },
        saveAsImage: { show: true }
      }
    },
    series: [
      {
        name: "新增确诊",
        type: 'pie',
        radius: [20, 140],
        center: ['25%', '50%'],
        roseType: 'radius',
        itemStyle: {
          borderRadius: 5
        },
        data: pro_add
      }, {
        name: "新增无症状",
        type: 'pie',
        radius: [20, 140],
        center: ['75%', '50%'],
        roseType: 'radius',
        itemStyle: {
          borderRadius: 5
        },
        data: pro_null
      }
    ]
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
        
        if (pro_add == '{}' || pro_add == '0') {
          alert("该天具体省份新增确诊数据未公示！（来源：国家卫生健康委员会）")
        }

        if (pro_null == '{}' || pro_null == '0') {
          alert("该天具体省份新增无症状数据未公示！（来源：国家卫生健康委员会）")
        }

        let mp1 = eval('(' + pro_add + ')');
        let mp2 = eval('(' + pro_null + ')');

        let data1 = new Array();
        for (let key in mp1) {
          data1.push({ name: key, value: mp1[key] })
        }

        let data2 = new Array();
        for (let key in mp2) {
          data2.push({ name: key, value: mp2[key] })
        }

        this.char.setOption(makeOption(data1, data2));
      })
    },
  }
}
</script>

