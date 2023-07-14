<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      message: '',
      characterLimit: 10000
    }
  }
})
</script>

<template>
  <div class="input-container">
    <input v-model="message" placeholder="prompt" />
    <div class="character-count">{{ message.length }} / {{ characterLimit }}</div>
  </div>
</template>

<style scoped>
.input-container {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px;
}

.input-container input {
  line-height: 2;
  width: 100%;
}

.character-count {
  text-align: left;
}
</style>
