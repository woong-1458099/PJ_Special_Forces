<template>
  <section>
    <h2>검색</h2>

    <div class="bar">
      <input v-model="q" placeholder="장소/컨셉 검색" />
      <button @click="search">검색</button>
    </div>

    <ul>
      <li v-for="p in results" :key="p.id" @click="$router.push(`/places/${p.id}`)" class="item">
        {{ p.name }}
      </li>
    </ul>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { placesAPI } from '@/api/places'

const q = ref('')
const results = ref([])

const search = async () => {
  try {
    const res = await placesAPI.search({ q: q.value })
    results.value = res.data
  } catch (e) {
    results.value = [
      { id: 1, name: '샘플 검색 결과 A' },
      { id: 2, name: '샘플 검색 결과 B' },
    ]
  }
}
</script>

<style scoped>
.bar { display:flex; gap:8px; }
.item { cursor:pointer; margin: 6px 0; }
</style>
