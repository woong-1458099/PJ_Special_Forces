import http from './http'

export const packagesAPI = {
  // 패키지 생성 (AI 추천)
  generate(payload) {
    return http.post('/api/v1/packages/generate/', payload)
  },

  // 내 패키지 목록
  listMine() {
    return http.get('/api/v1/packages/mine/')
  },

  // 패키지 저장
  save(payload) {
    return http.post('/api/v1/packages/', payload)
  },

  // 패키지 삭제
  remove(id) {
    return http.delete(`/api/v1/packages/${id}/`)
  },
}
