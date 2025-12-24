<template>
  <section class="container">
    <h1 class="title-center">Trip Connection</h1>
    <p class="subtitle-center">당신만의 완벽한 여행을 계획하세요</p>

    <!-- 검색 영역 -->
    <div class="search-section">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="여행지 검색..."
        class="search-input"
        @keyup.enter="handleSearch"
      />
      <button @click="handleSearch" class="search-btn">검색</button>
    </div>

    <!-- 예산 필터 -->
    <div class="budget-filter">
      <label>예산 범위:</label>
      <select v-model="selectedBudget" @change="applyBudgetFilter">
        <option value="">전체</option>
        <option value="30000">3만원 이하</option>
        <option value="50000">5만원 이하</option>
        <option value="100000">10만원 이하</option>
        <option value="200000">20만원 이하</option>
      </select>
    </div>

    <!-- 컨셉 카테고리 -->
    <h3 class="section-title">컨셉 선택</h3>
    <div class="grid-categories">
      <div
        v-for="c in concepts"
        :key="c.name"
        class="category-card"
        @click="goConcept(c)"
      >
        <span class="category-icon">{{ c.icon }}</span>
        <span class="category-name">{{ c.name }}</span>
      </div>
    </div>

    <!-- AI 추천 버튼 -->
    <div class="ai-recommend-section">
      <button @click="goAIRecommend" class="ai-btn">
        🤖 AI 맞춤 추천 받기
      </button>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { usePlacesStore } from '@/stores/places'

const router = useRouter()
const placesStore = usePlacesStore()

const searchQuery = ref('')
const selectedBudget = ref('')

const concepts = [
  { name: '액티비티', icon: '🏃', category: 'activity' },
  { name: '힐링', icon: '🧘', category: 'tourist' },
  { name: '카페', icon: '☕', category: 'restaurant' },
  { name: '쇼핑', icon: '🛍️', category: 'shopping' },
  { name: '맛집', icon: '🍽️', category: 'restaurant' },
  { name: '관광지', icon: '🏛️', category: 'tourist' }
]

const goConcept = (concept) => {
  placesStore.setConcept(concept.name)
  router.push({
    path: '/places',
    query: { category: concept.category }
  })
}

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    router.push({
      path: '/search',
      query: { q: searchQuery.value }
    })
  }
}

const applyBudgetFilter = () => {
  router.push({
    path: '/places',
    query: { budget: selectedBudget.value }
  })
}

const goAIRecommend = () => {
  router.push('/concept')
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.title-center {
  text-align: center;
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 16px;
  color: #2c3e50;
}

.subtitle-center {
  text-align: center;
  font-size: 18px;
  color: #7f8c8d;
  margin-bottom: 40px;
}

.search-section {
  display: flex;
  gap: 12px;
  max-width: 600px;
  margin: 0 auto 30px;
}

.search-input {
  flex: 1;
  padding: 16px 20px;
  font-size: 16px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  outline: none;
}

.search-input:focus {
  border-color: #4CAF50;
}

.search-btn {
  padding: 16px 32px;
  font-size: 16px;
  font-weight: bold;
  color: white;
  background: #4CAF50;
  border: none;
  border-radius: 12px;
  cursor: pointer;
}

.search-btn:hover {
  background: #45a049;
}

.budget-filter {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 40px;
}

.budget-filter label {
  font-weight: 600;
  color: #2c3e50;
}

.budget-filter select {
  padding: 10px 16px;
  font-size: 14px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
}

.section-title {
  text-align: center;
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 24px;
  color: #2c3e50;
}

.grid-categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.category-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 32px;
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.category-card:hover {
  border-color: #4CAF50;
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(76, 175, 80, 0.2);
}

.category-icon {
  font-size: 48px;
}

.category-name {
  font-size: 18px;
  font-weight: 600;
  color: #2c3e50;
}

.ai-recommend-section {
  text-align: center;
  margin-top: 40px;
}

.ai-btn {
  padding: 20px 48px;
  font-size: 20px;
  font-weight: bold;
  color: white;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  border-radius: 50px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
  transition: all 0.3s ease;
}

.ai-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}
</style>
