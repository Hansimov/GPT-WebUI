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
            const response = await axios.get(`${this.baseUrl}/api/messages?latest`)
            this.messages = response.data
        },
        async fetchLLMConfigs() {
            const response = await axios.get(`${this.baseUrl}/api/configs?llm`)
            this.llmConfigs = response.data
        },
        async handleKeyup(e: KeyboardEvent, message: any) {
            if (e.ctrlKey && e.key === 'Enter') {
                console.log(message.content)
                await axios.post(`${this.baseUrl}/api/messages`, {
                    model: message.model,
                    content: message.content,
                })
            }
        }
    }
})
