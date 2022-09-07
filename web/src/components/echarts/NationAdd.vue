<template>
  <div class="nation" ref="chart" style="height: 100%;width: 100%"></div>
</template>
 
<script>
export default {
  name: "TCPFlow",
  data() {
    return {
      option: {
        title: {
          text: 'TCP 流量监测'
        },
        grid: {
          x: 35,
          y: 35,
          x2: 35,
          y2: 35,
        },
        legend: {},
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: [],
          axisLabel: {
            show: false
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {}
        },
        series: [{
          name: 'TCP flow',
          type: 'line',
          data: [0],
          smooth: true,
          showSymbol: false,
          lineStyle: {
            width: 2,
            color: '#3b9a9c'
          },
          itemStyle: {
            color: '#ff6768'
          },
          areaStyle: {
            opacity: 0.8,
            color: '#B9EDF8'
          },
          markLine: {
            data: [{ type: 'average', name: 'Avg' }],
            lineStyle: { color: '#3b9a9c' }
          }
        }]
      }
    }
  },
  methods: {
    getData() {
      this.option.series[0].data.push(Math.random() * 2 + 3)
      const chart = this.$refs.chart;
      const myChart = this.$echarts.init(chart);
      myChart.setOption(this.option);
    }
  },
  mounted() {
    const chart = this.$refs.chart;
    const myChart = this.$echarts.init(chart);
    myChart.setOption(this.option);
  }
}
</script>
 
<style scoped>
div.nation {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>