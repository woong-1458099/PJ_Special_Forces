<template>
  <section>
    <h2>추천 장소 리스트</h2>
    <p>선택 컨셉: <b>{{ places.concept || '미선택' }}</b></p>

    <div class="bar">
      <select v-model="sort" @change="onChangeSort">
        <option value="rating">평점순</option>
        <option value="distance">거리순</option>
      </select>
      <button @click="refresh">새로고침</button>
    </div>

    <div v-if="loading">불러오는 중...</div>

    <div v-else class="list">
      <article
        v-for="p in places.list"
        :key="p.id"
        class="card"
        @click="goDetail(p.id)"
      >
        <h3>{{ p.name }}</h3>
        <p>카테고리: {{ p.category }}</p>
        <p>평점: {{ p.rating ?? '-' }}</p>
      </article>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { usePlacesStore } from '@/stores/places'

const router = useRouter()
const places = usePlacesStore()

const loading = ref(false)
const sort = ref(places.sort)

const onChangeSort = () => {
  places.setSort(sort.value)
  refresh()
}

const refresh = async () => {
  loading.value = true
  try {
    await places.fetchRecommend()
  } catch (e) {
    // 백엔드 없을 때도 화면이 죽지 않게
    places.list = [
      { id: 1, name: '샘플 장소 A', category: places.concept || '힐링', rating: 4.6 },
      { id: 2, name: '샘플 장소 B', category: places.concept || '카페', rating: 4.2 },
    ]
  } finally {
    loading.value = false
  }
}

const goDetail = (id) => router.push(`/places/${id}`)

onMounted(refresh)
</script>

<style scoped>
.bar { display:flex; gap:8px; align-items:center; }
.list { margin-top: 12px; display:grid; gap:12px; }
.card { border:1px solid #444; padding:12px; cursor:pointer; }
</style>
