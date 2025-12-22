import http from './http'

export const packagesAPI = {
  generate(payload) {
    return http.post('/api/v1/packages/generate', payload)
  },
  listMine() {
    return http.get('/api/v1/packages/mine')
  },
  save(payload) {
    return http.post('/api/v1/packages', payload)
  },
  remove(id) {
    return http.delete(`/api/v1/packages/${id}`)
  },
}
