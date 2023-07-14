<script lang="ts">
import { defineComponent } from 'vue'
import ChatHistory from '@/components/ChatHistory.vue'
import InputTextArea from '@/components/InputTextArea.vue'

export default defineComponent({
  components: {
    ChatHistory,
    InputTextArea
  }
})
</script>

<template>
  <div class="home-view">
    <ChatHistory />
    Hello World!<br />
    <InputTextArea />
  </div>
</template>

<style scoped>
.home-view {
  display: flex;
}

.home-view > * {
  flex: 1;
}
</style>
