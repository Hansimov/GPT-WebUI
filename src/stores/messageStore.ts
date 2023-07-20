import { defineStore } from 'pinia'
import axios from 'axios'


export const messageStore = defineStore({
    id: 'messages',
    state: () => ({
        messages: [],
        llmConfigs: {},
        baseUrl: "http://127.0.0.1:5000" // flask backend
    }),
    actions: {
        async fetchMessages() {
            const response = await axios.get(`${this.baseUrl}/messages`)
            this.messages = response.data
        },
        async fetchLLMConfigs() {
            const response = await axios.get(`${this.baseUrl}/llm_configs`)
            this.llmConfigs = response.data
        }
    }
})
