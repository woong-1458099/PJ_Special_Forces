<template>
  <section v-if="place">
    <h2>{{ place.name }}</h2>
    <p>{{ place.description || '설명 준비중' }}</p>

    <hr />

    <h3>운영시간</h3>
    <p>{{ place.opening_hours || '정보 없음' }}</p>

    <h3>지도</h3>
    <div class="map">지도 자리(카카오/구글 지도 나중에 연결)</div>

    <div class="btns">
      <button @click="addToPackage">패키지에 추가</button>
      <button @click="$router.push('/packages')">패키지 생성 페이지로</button>
    </div>
  </section>

  <div v-else>불러오는 중...</div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { usePlacesStore } from '@/stores/places'

const route = useRoute()
const places = usePlacesStore()

const place = computed(() => places.selected)

onMounted(async () => {
  try {
    await places.fetchDetail(route.params.id)
  } catch (e) {
    places.selected = {
      id: Number(route.params.id),
      name: '샘플 상세 장소',
      description: '백엔드 연결 전 임시 데이터',
      opening_hours: '10:00 ~ 20:00',
      lat: 37.5665,
      lng: 126.9780,
    }
  }
})

const addToPackage = () => {
  places.addToCart(place.value)
  alert('패키지에 담았어요(임시)')
}
</script>

<style scoped>
.map { height: 240px; border:1px dashed #666; display:flex; align-items:center; justify-content:center; }
.btns { margin-top: 12px; display:flex; gap:8px; }
</style>
