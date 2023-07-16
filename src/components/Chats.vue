<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  data: () => ({
    messages: [
      {
        role: 'user',
        content: 'What is your model?'
      },
      {
        role: 'GPT-4',
        content:
          "I am based on the GPT-4 model, which is a language model developed by OpenAI. GPT stands for Generative Pre-trained Transformer, and the '4' refers to the fourth iteration of this model series. Like its predecessors, GPT-4 is trained on a diverse range of internet text, but it's also fine-tuned with specific datasets to perform certain tasks."
      }
    ]
  })
})
</script>

<template>
  <div>
    <li v-for="message in messages">{{ message.role }}: {{ message.content }}</li>
  </div>
</template>
