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
          <button @click="quickSearch('제주도')" class="quick-filter-btn">
            🏝️ 제주도
          </button>
          <button @click="quickSearch('부산')" class="quick-filter-btn">
            🏖️ 부산
          </button>
          <button @click="quickSearch('서울')" class="quick-filter-btn">
            🏙️ 서울
          </button>
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
  { name: '쇼핑', icon: '🛍️', category: 'shopping' }
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
  height: 500px;
  background-image: url('https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=1920');
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
  background: rgba(139, 123, 209, 0.75);
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  color: white;
  max-width: 700px;
  padding: 20px;
}

.hero-title {
  font-size: 56px;
  font-weight: 700;
  margin-bottom: 12px;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
}

.hero-subtitle {
  font-size: 20px;
  margin-bottom: 36px;
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.3);
  font-weight: 400;
}

.hero-search {
  display: flex;
  gap: 0;
  max-width: 600px;
  margin: 0 auto 20px;
}

.hero-search-input {
  flex: 1;
  padding: 16px 24px;
  font-size: 16px;
  border: none;
  border-radius: 8px 0 0 8px;
  outline: none;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.hero-search-input::placeholder {
  color: #999;
}

.hero-search-btn {
  padding: 16px 32px;
  font-size: 16px;
  font-weight: 600;
  color: white;
  background: #5cb85c;
  border: none;
  border-radius: 0 8px 8px 0;
  cursor: pointer;
  transition: all 0.3s ease;
}

.hero-search-btn:hover {
  background: #4cae4c;
}

.quick-filters {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}

.quick-filter-btn {
  padding: 10px 20px;
  font-size: 15px;
  font-weight: 500;
  color: white;
  background: rgba(255, 255, 255, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.6);
  border-radius: 24px;
  cursor: pointer;
  backdrop-filter: blur(4px);
  transition: all 0.2s ease;
}

.quick-filter-btn:hover {
  background: rgba(255, 255, 255, 0.35);
  border-color: white;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 50px 20px;
}

.budget-filter {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 36px;
}

.budget-filter label {
  font-weight: 600;
  color: #333;
  font-size: 15px;
}

.budget-filter select {
  padding: 8px 16px;
  font-size: 14px;
  border: 2px solid #ddd;
  border-radius: 6px;
  cursor: pointer;
  background: white;
}

.budget-filter select:focus {
  outline: none;
  border-color: #5cb85c;
}

.section-title {
  text-align: center;
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 28px;
  color: #333;
}

.grid-categories {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 40px;
}

@media (max-width: 768px) {
  .grid-categories {
    grid-template-columns: repeat(2, 1fr);
  }
}

.category-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 36px 20px;
  background: white;
  border: 2px solid #e8e8e8;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.category-card:hover {
  border-color: #5cb85c;
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(92, 184, 92, 0.15);
}

.category-icon {
  font-size: 52px;
}

.category-name {
  font-size: 17px;
  font-weight: 600;
  color: #333;
}

.ai-recommend-section {
  text-align: center;
  margin-top: 48px;
}

.ai-btn {
  padding: 16px 40px;
  font-size: 18px;
  font-weight: 600;
  color: white;
  background: linear-gradient(135deg, #8b7bd1 0%, #a694d4 100%);
  border: none;
  border-radius: 50px;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(139, 123, 209, 0.4);
  transition: all 0.3s ease;
}

.ai-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(139, 123, 209, 0.5);
}
</style>
