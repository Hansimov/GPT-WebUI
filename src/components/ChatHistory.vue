<template>
  <div class="chat-history">
    <div
      v-for="entry in entries"
      :key="entry.id"
      class="chat-history-entry"
      @click="loadChatHistory(entry.id)"
    >
      {{ entry.name }}
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      entries: [
        { id: 1, name: 'Chat 1' },
        { id: 2, name: 'Chat 2' },
        { id: 3, name: 'Chat 3' }
      ]
    }
  },
  methods: {
    loadChatHistory(id) {
      // load chat history for the given id
    }
  }
})
</script>

<style scoped>
.chat-history {
  /* styles for the chat history container */
}

.chat-history-entry {
  /* styles for each chat history entry */
}
</style>
