import { defineStore } from 'pinia'
import { packagesAPI } from '@/api/packages'

export const usePackagesStore = defineStore('packages', {
  state: () => ({
    draft: null,
    mine: [],
  }),
  actions: {
    async generate(payload) {
      const res = await packagesAPI.generate(payload)
      this.draft = res.data
    },
    async fetchMine() {
      const res = await packagesAPI.listMine()
      this.mine = res.data
    },
    async save(payload) {
      const res = await packagesAPI.save(payload)
      return res.data
    },
    async remove(id) {
      await packagesAPI.remove(id)
      this.mine = this.mine.filter((p) => p.id !== id)
    },
  },
})
