<script setup>
import { useRouter } from 'vue-router'
import { usePlacesStore } from '@/stores/places'

const router = useRouter()
const places = usePlacesStore()

const onSelect = (c) => {
  places.setConcept(c)
  router.push('/explore')   // ✅ 컨셉 누르면 바로 추천으로 이동
}
</script>

<template>
  <h2>컨셉 선택</h2>
  <div>
    <button @click="onSelect('헬스')">헬스</button>
    <button @click="onSelect('힐링')">힐링</button>
    <button @click="onSelect('카페')">카페</button>
    <button @click="onSelect('쇼핑')">쇼핑</button>
    <button @click="onSelect('맛집')">맛집</button>
    <button @click="onSelect('산책')">산책</button>
  </div>
</template>
