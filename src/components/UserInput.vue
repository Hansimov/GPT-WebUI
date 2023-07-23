<script lang="ts">
import { defineComponent, computed } from 'vue'
import { messageStore } from '@/stores/messageStore'

export default defineComponent({
  setup() {
    const store = messageStore()

    return {
      handleKeyupInUserInput: store.handleKeyupInUserInput
    }
  },
  computed: {},
  methods: {}
})
</script>

<template>
  <v-footer app>
    <v-textarea
      class="user-input"
      density="compact"
      hide-details
      rows="1"
      auto-grow
      variant="outlined"
      @keyup="handleKeyupInUserInput($event)"
    ></v-textarea>
  </v-footer>
</template>
