<template>
  <div class="home-wrapper">
    <!-- 히어로 섹션 -->
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <h1 class="hero-title">Snow Travel</h1>
        <p class="hero-subtitle">당신의 여행을 특별하게 만들어 드립니다</p>

        <!-- 검색 영역 -->
        <div class="hero-search">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="어디로 떠나고 싶으세요?"
            class="hero-search-input"
            @keyup.enter="handleSearch"
          />
          <button @click="handleSearch" class="hero-search-btn">검색</button>
        </div>

        <!-- 빠른 필터 -->
        <div class="quick-filters">
          <button @click="quickSearch('제주도')" class="quick-filter-btn">🏝️ 제주도</button>
          <button @click="quickSearch('부산')" class="quick-filter-btn">🏖️ 부산</button>
          <button @click="quickSearch('서울')" class="quick-filter-btn">🏙️ 서울</button>
        </div>
      </div>
    </section>

    <!-- 메인 컨텐츠 -->
    <section class="container">

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
  </div>
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

const quickSearch = (location) => {
  searchQuery.value = location
  handleSearch()
}
</script>

<style scoped>
.home-wrapper {
  width: 100%;
}

/* 히어로 섹션 */
.hero-section {
  position: relative;
  height: 600px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  background-image: url('https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1920');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.7), rgba(118, 75, 162, 0.7));
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  color: white;
  max-width: 800px;
  padding: 20px;
}

.hero-title {
  font-size: 64px;
  font-weight: 900;
  margin-bottom: 16px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  letter-spacing: -1px;
}

.hero-subtitle {
  font-size: 24px;
  margin-bottom: 40px;
  text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
  font-weight: 300;
}

.hero-search {
  display: flex;
  gap: 12px;
  max-width: 600px;
  margin: 0 auto 24px;
}

.hero-search-input {
  flex: 1;
  padding: 20px 24px;
  font-size: 18px;
  border: none;
  border-radius: 50px;
  outline: none;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.hero-search-btn {
  padding: 20px 40px;
  font-size: 18px;
  font-weight: 600;
  color: white;
  background: #4CAF50;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.4);
  transition: all 0.3s ease;
}

.hero-search-btn:hover {
  background: #45a049;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.6);
}

.quick-filters {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.quick-filter-btn {
  padding: 12px 24px;
  font-size: 16px;
  font-weight: 500;
  color: white;
  background: rgba(255, 255, 255, 0.2);
  border: 2px solid rgba(255, 255, 255, 0.5);
  border-radius: 50px;
  cursor: pointer;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.quick-filter-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  border-color: white;
  transform: translateY(-2px);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 20px;
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
