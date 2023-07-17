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
        content:
          "I am GPT-3.5. I am based on the GPT-4 model, which is a language model developed by OpenAI. GPT stands for Generative Pre-trained Transformer, and the '4' refers to the fourth iteration of this model series. Like its predecessors, GPT-4 is trained on a diverse range of internet text, but it's also fine-tuned with specific datasets to perform certain tasks.I am based on the GPT-4 model, which is a language model developed by OpenAI. GPT stands for Generative Pre-trained Transformer, and the '4' refers to the fourth iteration of this model series. Like its predecessors, GPT-4 is trained on a diverse range of internet text, but it's also fine-tuned with specific datasets to perform certain tasks.I am based on the GPT-4 model, which is a language model developed by OpenAI. GPT stands for Generative Pre-trained Transformer, and the '4' refers to the fourth iteration of this model series. Like its predecessors, GPT-4 is trained on a diverse range of internet text, but it's also fine-tuned with specific datasets to perform certain tasks.I am based on the GPT-4 model, which is a language model developed by OpenAI. GPT stands for Generative Pre-trained Transformer, and the '4' refers to the fourth iteration of this model series. Like its predecessors, GPT-4 is trained on a diverse range of internet text, but it's also fine-tuned with specific datasets to perform certain tasks."
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
