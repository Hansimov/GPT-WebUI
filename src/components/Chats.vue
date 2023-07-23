<script lang="ts">
import { defineComponent, computed } from 'vue'
import { messageStore } from '@/stores/messageStore'

export default defineComponent({
  setup() {
    const store = messageStore()
    store.fetchMessages()
    const messages = computed(() => store.messages)
    // console.log(messages)
    store.fetchLLMConfigs()
    const llmConfigs = computed(() => store.llmConfigs)
    // console.log(llmConfigs)

    return {
      messages,
      llmConfigs,
      handleKeyup: store.handleKeyup
    }
  },
  computed: {},
  methods: {}
})
</script>

<template>
  <v-container
    fluid
    v-for="(message, idx) in messages"
    :key="idx"
    :class="{ 'user-chat': message.model === 'user', chat: message.model !== 'user' }"
  >
    <v-row align="start">
      <v-col cols="auto">
        <v-avatar>
          <v-img
            v-if="llmConfigs && llmConfigs[message.model]"
            :src="llmConfigs[message.model]['avatar']"
            :alt="llmConfigs[message.model]['name']"
          />
        </v-avatar>
      </v-col>
      <v-col>
        <v-textarea
          variant="plain"
          v-model="message.content"
          rows="1"
          hide-details
          auto-grow
          @keyup="handleKeyup($event, message)"
        ></v-textarea>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
/* classes of different models */
.user-chat {
  background-color: #383838;
}

/* padding and min-height of textarea of chats */
.v-input--density-default {
  --v-input-padding-top: 0px !important;
}
.v-field__input {
  min-height: calc(
    max(
        var(--v-input-control-height, 56px),
        1.5rem + var(--v-field-input-padding-top) + var(--v-field-input-padding-bottom)
      ) + var(--v-input-chips-margin-bottom) - 5px
  ) !important;
}
</style>
