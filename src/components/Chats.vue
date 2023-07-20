<script lang="ts">
import { defineComponent, watch, computed } from 'vue'
import { messageStore } from '@/stores/messageStore'

export default defineComponent({
  setup() {
    const store = messageStore()
    store.fetchMessages()
    const messages = computed(() => store.messages)
    // console.log(messages)
    store.fetchLLMConfigs()
    const llm_configs = computed(() => store.llm_configs)
    // console.log(llm_configs)

    return {
      messages,
      llm_configs
    }
  },
  computed: {},
  methods: {}
})
</script>

<template>
  <v-container fluid v-for="(message, idx) in messages" :key="idx" class="chat">
    <v-row align="start">
      <v-col cols="auto">
        <v-avatar>
          <v-img
            v-if="llm_configs && llm_configs[message.model]"
            :src="llm_configs[message.model]['avatar']"
            :alt="llm_configs[message.model]['name']"
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
        ></v-textarea>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
/* classes of different models */
.user-chats {
  /* background-color: lightgray; */
}
.gpt-35-chats {
  /* background-color: lightblue; */
}
.gpt-4-chats {
  /* background-color: lightcyan; */
}
.claude-2-chats {
  /* background-color: lightyellow; */
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
