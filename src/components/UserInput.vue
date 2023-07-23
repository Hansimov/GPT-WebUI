<script lang="ts">
import { defineComponent, computed } from 'vue'
import { messageStore } from '@/stores/messageStore'

export default defineComponent({
  data: () => ({
    userInputContent: ''
  }),
  setup() {
    const store = messageStore()
    return {
      handleKeyupInUserInput: store.handleKeyupInUserInput
    }
  },
  computed: {},
  methods: {
    clearUserInput() {
      this.userInputContent = ''
    }
  }
})
</script>

<template>
  <div id="user-input-container">
    <v-footer app>
      <v-textarea
        v-model="userInputContent"
        ref="userInput"
        class="user-input"
        density="compact"
        hide-details
        rows="1"
        auto-grow
        variant="outlined"
        @keyup="handleKeyupInUserInput($event, clearUserInput)"
      ></v-textarea>
    </v-footer>
  </div>
</template>
