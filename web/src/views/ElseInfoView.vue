<template>
  <div>
    <ContentField>
      <TestCharts></TestCharts>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '@/components/ContentField.vue';
import TestCharts from '@/components/MyCharts/testCharts.vue';
export default {
  components: { ContentField, TestCharts }
}
</script>

<style scoped>

</style>