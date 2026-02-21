import http from './http'

export const placesAPI = {
  // 장소 목록 조회 (카테고리, 검색어, 예산 필터 가능)
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

  // 예산 기반 필터링
  byBudget(budget) {
    return http.get('/api/v1/places/', {
      params: { budget }
    })
  },

  // AI 기반 추천
  recommend(preferences) {
    return http.post('/api/v1/places/recommend/', preferences)
  },

  // 랜덤 추천
  random(count = 5) {
    return http.get('/api/v1/places/', {
      params: { random: count }
    })
  },
}
