import { defineStore } from 'pinia'
import axios from 'axios'

export interface Message {
    model: string
    role: string
    content: string
}

export const messageStore = defineStore({
    id: 'messages',
    state: () => ({
        messages: [] as Message[],
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

        async handleKeyup(e: KeyboardEvent, message: Message) {
            if (e.ctrlKey && e.key === 'Enter') {
                console.log(message.content)
                const response = await axios.post(`${this.baseUrl}/api/messages`, {
                    model: message.model,
                    role: message.role,
                    content: message.content,
                })
                const response_message: Message = response.data.message
                console.log(response_message)
                this.messages.push(response_message)
            }
        }
    }
})
