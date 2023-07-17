<script lang="ts">
import { defineComponent } from 'vue'
import Chats from '@/components/Chats.vue'
import AppBar from '@/components/AppBar.vue'
import UserInput from '@/components/UserInput.vue'

export default defineComponent({
  components: {
    Chats,
    AppBar,
    UserInput
  },
  data: () => ({})
})
</script>

<template>
  <v-app>
    <AppBar />

    <v-main>
      <Chats />
    </v-main>

    <UserInput />
  </v-app>
</template>

<style></style>
