<script lang="ts">
import { defineComponent } from 'vue'
interface ConfigsOfRole {
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
        role: 'claude-2',
        content: 'I am Claude-2'
      }
    ],
    class_of_role: {
      user: 'user-chats',
      'gpt-3.5': 'gpt-35-chats',
      'gpt-4': 'gpt-4-chats',
      'claude-2': 'Claude2-chats'
    } as ConfigsOfRole,
    avatar_of_role: {
      user: 'src/assets/user.png',
      'claude-2': 'src/assets/claude.png',
      'gpt-3.5': 'src/assets/gpt-3.5.png',
      'gpt-4': 'src/assets/gpt-4.png'
    } as ConfigsOfRole,
    display_name_of_role: {
      user: 'User',
      claude2: 'Claude-2',
      'gpt-3.5': 'GPT-3.5',
      'gpt-4': 'GPT-4'
    }
  }),
  computed: {},
  methods: {
    async getAvatar(role: string) {
      const avatarPath = this.avatar_of_role[role]
      if (avatarPath) {
        const module = await import(avatarPath)
        return module.default
      }
    }
  }
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
      <v-row>
        <v-col cols="auto">
          <v-avatar>
            <v-img :src="avatar_of_role[message.role]" :alt="message.role" />
          </v-avatar>
        </v-col>
        <v-col> {{ message.role }}: {{ message.content }} </v-col>
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
.Claude2-chats {
  background-color: lightyellow;
}
</style>
