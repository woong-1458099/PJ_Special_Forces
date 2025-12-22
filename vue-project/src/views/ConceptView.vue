<template>
  <section>
    <h2>컨셉 선택</h2>

    <div class="grid">
      <button
        v-for="c in concepts"
        :key="c"
        :class="{ active: places.concept === c }"
        @click="places.setConcept(c)"
      >
        {{ c }}
      </button>
    </div>

    <hr />

    <h3>필터</h3>
    <div class="filters">
      <label>예산 <input type="number" v-model.number="budget" placeholder="예: 50000" /></label>
      <label>거리(km) <input type="number" v-model.number="distance" placeholder="예: 5" /></label>
      <label>
        시간대
        <select v-model="time">
          <option value="">선택</option>
          <option value="morning">아침</option>
          <option value="afternoon">점심</option>
          <option value="evening">저녁</option>
        </select>
      </label>
    </div>

    <button class="go" @click="applyAndGo">추천 받기</button>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { usePlacesStore } from '@/stores/places'

const router = useRouter()
const places = usePlacesStore()

const concepts = ['헬스', '힐링', '카페', '쇼핑', '맛집', '산책']

const budget = ref(null)
const distance = ref(null)
const time = ref('')

const applyAndGo = () => {
  places.setFilters({ budget: budget.value, distance: distance.value, time: time.value })
  router.push('/places')
}
</script>

<style scoped>
.grid { display:flex; flex-wrap:wrap; gap:8px; }
.grid button.active { border: 2px solid #fff; }
.filters { display:grid; gap:10px; max-width: 420px; }
.go { margin-top: 12px; }
</style>
