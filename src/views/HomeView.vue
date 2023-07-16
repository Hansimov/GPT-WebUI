<script lang="ts">
import { defineComponent } from 'vue'
import Chats from '@/components/Chats.vue'

export default defineComponent({
  components: {
    Chats
  },
  data: () => ({
    left_sidebar_visible: true,
    right_sidebar_visible: true,
    app_bar_title: 'GPT WebUI'
  })
})
</script>

<template>
  <v-app>
    <v-navigation-drawer v-model="left_sidebar_visible"> </v-navigation-drawer>
    <v-navigation-drawer location="right" v-model="right_sidebar_visible">
      <v-list>
        <v-list-item v-for="n in 5" :key="n" :title="`Prompt ${n}`" link> </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar height="30" flat>
      <v-icon
        size="large"
        :icon="left_sidebar_visible ? 'fa fa-angle-double-left' : 'fa fa-angle-double-right'"
        color="cyan"
        end="true"
        @click="left_sidebar_visible = !left_sidebar_visible"
      ></v-icon>
      <v-toolbar-title :text="app_bar_title" class="d-flex justify-center"></v-toolbar-title>
      <v-icon
        size="large"
        :icon="right_sidebar_visible ? 'fa fa-angle-double-right' : 'fa fa-angle-double-left'"
        color="cyan"
        start="true"
        @click="right_sidebar_visible = !right_sidebar_visible"
      ></v-icon>
    </v-app-bar>

    <v-main>
      <Chats />
    </v-main>

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
</style>
