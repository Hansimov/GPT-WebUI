<script lang="ts">
import { defineComponent } from 'vue'
import { SidebarMenu } from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

export default defineComponent({
  data: () => {
    return {
      menu: [
        {
          header: 'Chat History',
          hiddenOnCollapse: true
        },
        {
          href: '/',
          title: 'Dashboard',
          icon: 'fa fa-user'
        }
      ]
    }
  },
  components: {
    SidebarMenu
  },
  methods: {
    loadChatHistory(id) {
      // load chat history for the given id
    }
  }
})
</script>

<template>
  <div class="chat-history">
    <sidebar-menu :menu="menu" />
  </div>
</template>

<style scoped>
.chat-history {
  /* styles for the chat history container */
}

.chat-history-entry {
  /* styles for each chat history entry */
}
</style>
