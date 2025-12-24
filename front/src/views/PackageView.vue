<template>
  <section>
    <h2>패키지 생성(여행 코스)</h2>

    <h3>담은 장소</h3>
    <ul>
      <li v-for="p in places.cart" :key="p.id">
        {{ p.name }}
        <button @click="places.removeFromCart(p.id)">빼기</button>
      </li>
    </ul>

    <div class="btns">
      <button @click="generate" :disabled="places.cart.length === 0">자동 코스 생성</button>
      <button @click="places.clearCart()">비우기</button>
    </div>

    <div v-if="packages.draft" class="result">
      <h3>생성된 코스(임시 출력)</h3>
      <pre>{{ JSON.stringify(packages.draft, null, 2) }}</pre>
      <button @click="save">코스 저장</button>
    </div>
  </section>
</template>

<script setup>
import { usePlacesStore } from '@/stores/places'
import { usePackagesStore } from '@/stores/packages'

const places = usePlacesStore()
const packages = usePackagesStore()

const generate = async () => {
  const payload = {
    concept: places.concept,
    placeIds: places.cart.map((p) => p.id),
    // 시간표/루트 옵션은 나중에 추가
  }

  try {
    await packages.generate(payload)
  } catch (e) {
    packages.draft = {
      title: '샘플 코스',
      concept: places.concept,
      items: places.cart.map((p, idx) => ({
        order: idx + 1,
        placeId: p.id,
        name: p.name,
        time: `${10 + idx}:00`,
      })),
    }
  }
}

const save = async () => {
  try {
    await packages.save(packages.draft)
    alert('저장 완료')
  } catch (e) {
    alert('백엔드 연결 전이라 저장은 임시입니다.')
  }
}
</script>

<style scoped>
.btns { margin-top: 10px; display:flex; gap:8px; }
.result { margin-top: 12px; border:1px solid #444; padding:12px; }
</style>
