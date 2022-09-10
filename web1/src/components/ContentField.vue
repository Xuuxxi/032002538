<template>
  <div class="container content-field">
    <div class="card">
      <div class="card-body">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
div.content-field{
  width: 80%;
  height: 80%;
  margin-top: 20px;
}
</style>