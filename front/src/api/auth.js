import http from './http'

export const authAPI = {
  login(payload) {
    return http.post('/api/v1/auth/login/', payload)
  },
  signup(payload) {
    return http.post('/api/v1/auth/signup/', payload)
  },
  me() {
    return http.get('/api/v1/auth/me/')
  },
}
