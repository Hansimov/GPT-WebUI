<script lang="ts">
import { defineComponent } from 'vue'
import ChatHistory from '@/components/ChatHistory.vue'
import UserInput from '@/components/UserInput.vue'

export default defineComponent({
  components: {
    UserInput
  },
  data: () => ({
    left_side_bar_visible: false,
    right_side_bar_visible: false
  })
})
</script>

<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="left_side_bar_visible"> </v-navigation-drawer>
    <v-app-bar>
      <v-icon
        center
        size="large"
        icon="$vuetify"
        color="cyan"
        start="true"
        end="true"
        @click="left_side_bar_visible = !left_side_bar_visible"
      ></v-icon>
      <v-icon
        center
        size="large"
        icon="fa fa-user"
        color="green"
        start="true"
        end="true"
        @click="right_side_bar_visible = !right_side_bar_visible"
      ></v-icon>
    </v-app-bar>

    <v-main>Hello World</v-main>

    <v-navigation-drawer location="right" v-model="right_side_bar_visible">
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
