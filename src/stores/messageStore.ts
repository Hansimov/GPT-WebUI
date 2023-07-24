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
        async handleKeyupInChat(e: KeyboardEvent, message: Message) {
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
                this.scrollChatsToBottom()
            }
        },
        async scrollChatsToBottom() {
            setTimeout(() => {
                const lastMessage = document.querySelector('#chats-container > :last-child');
                if (lastMessage) {
                    lastMessage.scrollIntoView({ behavior: 'smooth' });
                }
            }, 100);
        },
        async *streamResponse(response: Response) {
            const reader = response.body!.getReader()
            let result = ''
            while (true) {
                const { done, value } = await reader.read()
                result += new TextDecoder().decode(value)
                if (done) break
                try {
                    const response_chunk: Message = JSON.parse(result)
                    console.log(response_chunk)
                    yield response_chunk
                    result = ''
                } catch (e) { }
            }
            console.log("Response stream ended.")
        },
        async handleKeyupInUserInput(e: KeyboardEvent, clearUserInput: () => void) {
            const input_content = (e.target as HTMLInputElement).value
            if (e.key === 'Enter' && !e.shiftKey) {
                if (input_content.trim() !== '') {
                    console.log(input_content)
                    const input_message: Message = {
                        model: "user",
                        role: "user",
                        content: input_content.replace(/^\n+|\n+$/g, ''),
                    }
                    this.messages.push(input_message)
                    this.scrollChatsToBottom()
                    clearUserInput()
                    this.messages.push(
                        { "role": "gpt-4", "model": "gpt-4", "content": "Thinking..." }
                    )

                    const response = await fetch(`${this.baseUrl}/api/messages`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(input_message)
                    })
                    for await (const response_chunk of this.streamResponse(response)) {
                        if (response_chunk.delta.role) {
                            this.messages[this.messages.length - 1].role = response_chunk.delta.role
                            this.messages[this.messages.length - 1].content = ""
                        }
                        if (response_chunk.delta.model) {
                            this.messages[this.messages.length - 1].model = response_chunk.delta.model
                            this.messages[this.messages.length - 1].content = ""
                        }
                        if (response_chunk.delta.content) {
                            this.messages[this.messages.length - 1].content += response_chunk.delta.content
                        }
                        this.scrollChatsToBottom()
                    }
                } else {
                    alert("Input cannot be empty.")
                }
            }
        },
    }
})
