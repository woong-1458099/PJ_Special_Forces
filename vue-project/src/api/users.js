import http from './http'

export const usersAPI = {
  // 사용자 프로필 조회 (향후 구현 예정)
  getProfile(userId) {
    return http.get(`/api/v1/users/${userId}/`)
  },

  // 사용자 정보 업데이트 (향후 구현 예정)
  updateProfile(userId, payload) {
    return http.put(`/api/v1/users/${userId}/`, payload)
  },
}
