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
    <v-navigation-drawer location="left" v-model="left_sidebar_visible">
      <v-list>
        <v-list-item v-for="n in 8" :key="n" :title="`History ${n}`" link> </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar density="compact" flat>
      <v-icon
        :icon="left_sidebar_visible ? 'fa fa-angle-double-left' : 'fa fa-angle-double-right'"
        end="true"
        @click="left_sidebar_visible = !left_sidebar_visible"
      ></v-icon>
      <v-toolbar-title :text="app_bar_title" class="d-flex justify-center"></v-toolbar-title>
      <v-icon
        :icon="right_sidebar_visible ? 'fa fa-angle-double-right' : 'fa fa-angle-double-left'"
        start="true"
        @click="right_sidebar_visible = !right_sidebar_visible"
      ></v-icon>
    </v-app-bar>

    <v-navigation-drawer location="right" v-model="right_sidebar_visible">
      <v-list>
        <v-list-item v-for="n in 5" :key="n" :title="`Prompt ${n}`" link> </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <Chats />
    </v-main>

    <v-footer app>
      <v-textarea
        class="user-input"
        density="compact"
        hide-details
        rows="1"
        auto-grow
        variant="outlined"
      ></v-textarea>
    </v-footer>
  </v-app>
</template>

<style scoped>
/* 
  A Complete Guide to Flexbox | CSS-Tricks - CSS-Tricks
    * https://css-tricks.com/snippets/css/a-guide-to-flexbox/ 
*/
</style>
