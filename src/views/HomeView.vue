<script lang="ts">
import { defineComponent } from 'vue'
import ChatHistory from '@/components/ChatHistory.vue'
import UserInput from '@/components/UserInput.vue'

export default defineComponent({
  components: {
    UserInput
  }
})
</script>
<!-- 
<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <ChatHistory class="chat-history" />
      </v-col>
      <v-col cols="3">
        <div class="messages">Hello World!</div>
      </v-col>
      <v-col cols="6">
        <UserInput class="user-input" />
      </v-col>
    </v-row>
  </v-container>
</template>
-->

<template>
  <v-app id="inspire">
    <v-system-bar>
      <v-spacer></v-spacer>

      <v-icon>mdi-square</v-icon>

      <v-icon>mdi-circle</v-icon>

      <v-icon>mdi-triangle</v-icon>
    </v-system-bar>

    <v-navigation-drawer color="grey-lighten-3" rail>
      <v-avatar class="d-block text-center mx-auto mt-4" color="grey-darken-1" size="36"></v-avatar>

      <v-divider class="mx-3 my-5"></v-divider>

      <v-avatar
        v-for="n in 6"
        :key="n"
        class="d-block text-center mx-auto mb-9"
        color="grey-lighten-1"
        size="28"
      ></v-avatar>
    </v-navigation-drawer>

    <v-navigation-drawer width="244">
      <v-sheet color="grey-lighten-5" height="128" width="100%"></v-sheet>

      <v-list>
        <v-list-item v-for="n in 5" :key="n" :title="`Item ${n}`" link> </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar class="px-3" color="grey-lighten-4" flat height="72">
      <v-spacer></v-spacer>

      <v-responsive max-width="156">
        <v-text-field
          bg-color="grey-lighten-2"
          class="rounded-pill overflow-hidden"
          density="compact"
          hide-details
          variant="solo"
        ></v-text-field>
      </v-responsive>
    </v-app-bar>

    <v-main>Hello World</v-main>

    <v-navigation-drawer location="right">
      <v-list>
        <v-list-item v-for="n in 5" :key="n" :title="`Item ${n}`" link> </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-footer app height="72">
      <v-text-field
        bg-color="grey-lighten-1"
        class="rounded-pill overflow-hidden"
        density="compact"
        hide-details
        variant="solo"
      ></v-text-field>
    </v-footer>
  </v-app>
</template>

<style scoped>
/* 
  A Complete Guide to Flexbox | CSS-Tricks - CSS-Tricks
    * https://css-tricks.com/snippets/css/a-guide-to-flexbox/ 
*/
.home-view {
  /* display: flex; */
  /* height: 97vh; */
  /* justify-content: space-evenly; */
  border: solid blue;
}

.chat-history {
  /* flex: 1; */
  /* order: 0; */
  /* align-self: flex-start; */
  border: solid red;
}
.messages {
  /* flex: 1; */
  /* align-self: flex-end; */
  border: solid green;
}

.user-input {
  /* flex: 1;
  align-self: flex-end; */
  border: solid yellow;
  /* order: 1; */
  /* flex-shrink: 1; */
  /* margin-bottom: auto; */
}
</style>
