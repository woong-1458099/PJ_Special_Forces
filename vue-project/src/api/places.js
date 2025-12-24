import http from './http'

export const placesAPI = {
  recommend(params) {
    // params: concept, budget, distance, time, lat, lng ...
    return http.get('/api/v1/places/recommend', { params })
  },
  detail(id) {
    return http.get(`/api/v1/places/${id}/`)
  },
  search(params) {
    return http.get('/api/v1/places/search', { params })
  },
}
