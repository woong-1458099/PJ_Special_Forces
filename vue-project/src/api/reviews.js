import http from './http'

export const reviewsAPI = {
  // 장소별 리뷰 목록
  listByPlace(placeId) {
    return http.get(`/api/v1/reviews/places/${placeId}/`)
  },

  // 리뷰 작성
  create(placeId, payload) {
    return http.post(`/api/v1/reviews/places/${placeId}/create/`, payload)
  },
}
