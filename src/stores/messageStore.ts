import { defineStore } from 'pinia'
import axios from 'axios'

export const messageStore = defineStore({
    id: 'messages',
    state: () => ({
        data: []
    }),
    actions: {
        async fetchData() {
            const response = await axios.get('http://127.0.0.1:5000/messages')
            this.data = response.data
        }
    }
})
