<template>
  <ContentField>
    <div class="welcome">欢迎来到我的网站, 请夸奖我的背景选择以继续 -> <button class="btn btn-primary" @click="reload()">夸奖</button></div>
    
  </ContentField>
</template>

<script>
import ContentField from '@/components/ContentField.vue';
import router from '@/router';
export default {
    components: { ContentField },
    methods: {
      reload(){
        router.push('/nation')
      }
    }
}
</script>

<style>
div.welcome {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>