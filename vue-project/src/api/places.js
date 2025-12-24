import http from './http'

export const placesAPI = {
  // 장소 목록 조회 (카테고리, 검색어 필터 가능)
  list(params) {
    return http.get('/api/v1/places/', { params })
  },

  // 장소 상세 조회
  detail(id) {
    return http.get(`/api/v1/places/${id}/`)
  },

  // 장소 검색
  search(searchQuery) {
    return http.get('/api/v1/places/', {
      params: { search: searchQuery }
    })
  },

  // 카테고리별 조회
  byCategory(category) {
    return http.get('/api/v1/places/', {
      params: { category }
    })
  },
}
