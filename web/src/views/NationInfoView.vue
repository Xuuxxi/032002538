<template>
  <div>
    <ContentField>
      <NationInfoCharts></NationInfoCharts>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '@/components/ContentField.vue';
import NationInfoCharts from '@/components/MyCharts/NationInfoCharts.vue';

export default {
  components: { ContentField, NationInfoCharts }
}
</script>

<style scoped>

</style>