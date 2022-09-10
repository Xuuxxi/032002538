<template>
  <div>
    <ContentField>
      <ProInfoCharts></ProInfoCharts>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '@/components/ContentField.vue';
import ProInfoCharts from '@/components/MyCharts/ProInfoCharts.vue';
export default {
    components: { ContentField, ProInfoCharts }
}
</script>

<style scoped>

</style>