<script lang="ts">
import { defineComponent } from 'vue'

interface LLMConfig {
  name: string
  class: string
  avatar: string
}

interface LLMConfigs {
  [key: string]: LLMConfig
}

export default defineComponent({
  data: () => ({
    messages: [
      {
        model: 'user',
        role: 'user',
        content: 'What is your model?'
      },
      {
        model: 'gpt-4',
        role: 'llm',
        content:
          "I am based on the GPT-4 model, which is a language model developed by OpenAI. GPT stands for Generative Pre-trained Transformer, and the '4' refers to the fourth iteration of this model series. Like its predecessors, GPT-4 is trained on a diverse range of internet text, but it's also fine-tuned with specific datasets to perform certain tasks."
      },
      {
        model: 'gpt-3.5',
        role: 'llm',
        content: 'I am GPT-3.5'
      },
      {
        model: 'claude-2',
        role: 'llm',
        content: 'I am Claude-2'
      }
    ],
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
  }),
  computed: {},
  methods: {}
})
</script>

<template>
  <div>
    <v-container
      fill-height
      fluid
      v-for="(message, idx) in messages"
      :key="idx"
      :class="llm_configs[message.model]['class']"
    >
      <v-row align="center">
        <v-col cols="auto">
          <v-avatar>
            <v-img
              :src="llm_configs[message.model]['avatar']"
              :alt="llm_configs[message.model]['name']"
            />
          </v-avatar>
        </v-col>
        <v-col><v-card variant="text" :text="message.content"></v-card></v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style>
.user-chats {
  background-color: lightgray;
}
.gpt-35-chats {
  background-color: lightblue;
}
.gpt-4-chats {
  background-color: lightcyan;
}
.claude-2-chats {
  background-color: lightyellow;
}
</style>
