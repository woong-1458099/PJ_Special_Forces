import { defineStore } from 'pinia'
import { authAPI } from '@/api/auth'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    user: null,
  }),
  getters: {
    isLogin: (state) => !!state.token,
  },
  actions: {
    async login({ username, password }) {
      const res = await authAPI.login({ username, password })
      this.token = res.data.access || res.data.token || ''
      localStorage.setItem('token', this.token)
      await this.fetchMe()
    },
    async fetchMe() {
      const res = await authAPI.me()
      this.user = res.data
    },
    logout() {
      this.token = ''
      this.user = null
      localStorage.removeItem('token')
    },
  },
})
