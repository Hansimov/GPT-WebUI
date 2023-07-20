import { defineStore } from 'pinia'
import axios from 'axios'


export const messageStore = defineStore({
    id: 'messages',
    state: () => ({
        messages: [],
        llm_configs: {}
    }),
    actions: {
        async fetchMessages() {
            const response = await axios.get('http://127.0.0.1:5000/messages')
            this.messages = response.data
        },
        async fetchLLMConfigs() {
            const response = await axios.get('http://127.0.0.1:5000/llm_configs')
            this.llm_configs = response.data
        }
    }
})
