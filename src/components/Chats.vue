<script lang="ts">
import { defineComponent, watch, computed } from 'vue'
import { messageStore } from '@/stores/messageStore'

interface LLMConfig {
  name: string
  class: string
  avatar: string
}

interface LLMConfigs {
  [key: string]: LLMConfig
}

export default defineComponent({
  setup() {
    const store = messageStore()
    store.fetchData()
    const messages = computed(() => store.data)

    // let messages = store.data
    // console.log(messages)

    // watch(
    //   () => store.data,
    //   (newData) => {
    //     messages = newData
    //     console.log(messages)
    //   }
    // )

    return {
      messages,
      llm_configs: {
        user: {
          name: 'User',
          class: 'user-chats',
          avatar: 'src/assets/user.png'
        },
        'gpt-3.5': {
          name: 'GPT-3.5',
          class: 'gpt-35-chats',
          avatar: 'src/assets/gpt-3.5.png'
        },
        'gpt-4': {
          name: 'GPT-4',
          class: 'gpt-4-chats',
          avatar: 'src/assets/gpt-4.png'
        },
        'claude-2': {
          name: 'Claude-2',
          class: 'claude-2-chats',
          avatar: 'src/assets/claude-2.png'
        }
      } as LLMConfigs
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
