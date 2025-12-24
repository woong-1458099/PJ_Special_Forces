<template>
  <div class="home-wrapper">
    <!-- 히어로 섹션 -->
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <h1 class="hero-title">Snow Travel</h1>

        <!-- 검색 영역 -->
        <div class="search-container">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="어디로 여행을 떠나고 싶으세요?"
            class="search-input"
            @keyup.enter="handleSearch"
          />
          <button @click="handleSearch" class="search-btn">검색</button>
        </div>

        <!-- 탭 메뉴 -->
        <div class="tabs">
          <button :class="['tab-btn', { active: activeTab === 'recent' }]" @click="activeTab = 'recent'">
            📝 최근 검색
          </button>
          <button :class="['tab-btn', { active: activeTab === 'realtime' }]" @click="activeTab = 'realtime'">
            🔥 실시간 검색어
          </button>
          <button :class="['tab-btn', { active: activeTab === 'popular' }]" @click="activeTab = 'popular'">
            ⭐ 인기 여행지
          </button>
        </div>
      </div>
    </section>

    <!-- 카테고리 섹션 -->
    <section class="categories-section">
      <h3 class="section-title">여행 카테고리</h3>
      <div class="categories-grid">
        <div class="category-card" @click="goCategory('discount')">
          <div class="category-icon">🎁</div>
          <div class="category-name">무료 할인</div>
          <p class="category-desc">할인 혜택 가득한 여행 상품</p>
        </div>
        <div class="category-card" @click="goCategory('latest')">
          <div class="category-icon">✨</div>
          <div class="category-name">최신 여행</div>
          <p class="category-desc">새로 나온 여행 상품 모음</p>
        </div>
        <div class="category-card" @click="goCategory('honeymoon')">
          <div class="category-icon">💑</div>
          <div class="category-name">신혼 여행</div>
          <p class="category-desc">로맨틱한 신혼여행 패키지</p>
        </div>
      </div>
    </section>

    <!-- AI 추천 섹션 -->
    <section class="ai-section">
      <button @click="goAIRecommend" class="ai-recommend-btn">
        🤖 AI 맞춤 여행 추천 받기
      </button>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const searchQuery = ref('')
const activeTab = ref('recent')

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    router.push({
      path: '/search',
      query: { q: searchQuery.value }
    })
  }
}

const goCategory = (category) => {
  router.push({
    path: '/places',
    query: { category }
  })
}

const goAIRecommend = () => {
  router.push('/concept')
}
</script>

<style scoped>
.home-wrapper {
  width: 100%;
  min-height: 100vh;
  background: #f5f5f5;
}

/* 히어로 섹션 */
.hero-section {
  position: relative;
  height: 450px;
  background-image: url('https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?w=1920');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(120, 100, 180, 0.7);
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  width: 100%;
  max-width: 700px;
  padding: 20px;
}

.hero-title {
  font-size: 48px;
  font-weight: 700;
  color: white;
  margin-bottom: 32px;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
}

/* 검색 영역 */
.search-container {
  display: flex;
  max-width: 600px;
  margin: 0 auto 24px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  overflow: hidden;
}

.search-input {
  flex: 1;
  padding: 16px 20px;
  font-size: 15px;
  border: none;
  outline: none;
}

.search-input::placeholder {
  color: #999;
}

.search-btn {
  padding: 16px 32px;
  font-size: 15px;
  font-weight: 600;
  color: white;
  background: #5cb85c;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

.search-btn:hover {
  background: #4cae4c;
}

/* 탭 메뉴 */
.tabs {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.tab-btn {
  padding: 10px 20px;
  font-size: 14px;
  font-weight: 500;
  color: white;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.4);
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s;
  backdrop-filter: blur(4px);
}

.tab-btn:hover,
.tab-btn.active {
  background: rgba(255, 255, 255, 0.35);
  border-color: white;
}

/* 카테고리 섹션 */
.categories-section {
  max-width: 1000px;
  margin: 60px auto;
  padding: 0 20px;
}

.section-title {
  font-size: 24px;
  font-weight: 700;
  color: #333;
  margin-bottom: 32px;
  text-align: center;
}

.categories-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

@media (max-width: 768px) {
  .categories-grid {
    grid-template-columns: 1fr;
  }
}

.category-card {
  background: white;
  padding: 32px 24px;
  border-radius: 12px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.category-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.category-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.category-name {
  font-size: 20px;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
}

.category-desc {
  font-size: 14px;
  color: #666;
  line-height: 1.5;
}

/* AI 추천 섹션 */
.ai-section {
  text-align: center;
  padding: 40px 20px 80px;
}

.ai-recommend-btn {
  padding: 18px 48px;
  font-size: 18px;
  font-weight: 600;
  color: white;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  border-radius: 50px;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(102, 126, 234, 0.4);
  transition: all 0.3s;
}

.ai-recommend-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
}
</style>
