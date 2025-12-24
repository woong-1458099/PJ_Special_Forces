import { defineStore } from 'pinia'
import { placesAPI } from '@/api/places'

export const usePlacesStore = defineStore('places', {
  state: () => ({
    concept: '',
    filters: { budget: null, distance: null, time: '' },
    sort: 'rating',
    list: [],
    selected: null,
    cart: [], 
  }),
  actions: {
    setConcept(c) { this.concept = c },
    setFilters(f) { this.filters = { ...this.filters, ...f } },
    setSort(s) { this.sort = s },

    async fetchRecommend({ lat = 37.5665, lng = 126.9780 } = {}) {
      const params = { concept: this.concept, lat, lng, ...this.filters, sort: this.sort }
      const res = await placesAPI.recommend(params)
      this.list = res.data
    },

    async fetchDetail(id) {
      const res = await placesAPI.detail(id)
      this.selected = res.data
    },

    addToCart(place) {
      if (this.cart.some((p) => p.id === place.id)) return
      this.cart.push(place)
    },
    removeFromCart(id) {
      this.cart = this.cart.filter((p) => p.id !== id)
    },
    clearCart() {
      this.cart = []
    },
  },
})
