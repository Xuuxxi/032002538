<template>
  <div>
    <ContentField>
      <ElseInfoCharts></ElseInfoCharts>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '@/components/ContentField.vue';
import ElseInfoCharts from '@/components/MyCharts/ElseInfoCharts.vue';
export default {
  components: { ContentField, ElseInfoCharts }
}
</script>

<style scoped>

</style>