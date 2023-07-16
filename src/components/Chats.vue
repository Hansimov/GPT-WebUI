<script lang="ts">
import { defineComponent } from 'vue'
interface ClassOfRole {
  [key: string]: string
}

export default defineComponent({
  data: () => ({
    messages: [
      {
        role: 'user',
        content: 'What is your model?'
      },
      {
        role: 'gpt-4',
        content:
          "I am based on the GPT-4 model, which is a language model developed by OpenAI. GPT stands for Generative Pre-trained Transformer, and the '4' refers to the fourth iteration of this model series. Like its predecessors, GPT-4 is trained on a diverse range of internet text, but it's also fine-tuned with specific datasets to perform certain tasks."
      },
      {
        role: 'gpt-3.5',
        content: 'I am GPT-3.5'
      },
      {
        role: 'Claude2',
        content: 'I am Claude2'
      }
    ],
    class_of_role: {
      user: 'user-chats',
      'gpt-3.5': 'gpt-35-chats',
      'gpt-4': 'gpt-4-chats',
      Claude2: 'Claude2-chats'
    } as ClassOfRole
  }),
  computed: {}
})
</script>

<template>
  <div>
    <v-container
      fluid
      v-for="(message, idx) in messages"
      :key="idx"
      :class="class_of_role[message.role]"
    >
      {{ message.role }}: {{ message.content }}
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
.Claude2-chats {
  background-color: lightyellow;
}
</style>
