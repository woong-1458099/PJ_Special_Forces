<template>
  <div class="home-wrapper">
    <!-- 네비게이션 -->
    <nav class="top-nav">
      <div class="nav-buttons">
        <button class="nav-btn" @click="$router.push('/concept')">컨셉</button>
        <button class="nav-btn active" @click="$router.push('/')">추천</button>
        <button class="nav-btn" @click="$router.push('/places')">코스</button>
        <button class="nav-btn" @click="$router.push('/mypage')">마이</button>
      </div>
    </nav>

    <!-- 히어로 섹션 -->
    <section class="hero-section">
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

        <!-- 탭 버튼 -->
        <div class="tab-buttons">
          <button class="tab-btn">📝 최근 검색</button>
          <button class="tab-btn">🔥 실시간 검색어</button>
          <button class="tab-btn">⭐ 인기 여행지</button>
        </div>
      </div>
    </section>

    <!-- 카테고리 섹션 -->
    <section class="category-section">
      <h2 class="section-title">여행 카테고리</h2>

      <div class="category-grid">
        <div class="category-card" @click="goCategory('discount')">
          <div class="card-icon">🎁</div>
          <div class="card-content">
            <h3 class="card-title">무료 할인</h3>
            <p class="card-desc">할인 혜택 가득한 여행 상품</p>
          </div>
        </div>

        <div class="category-card" @click="goCategory('new')">
          <div class="card-icon">✨</div>
          <div class="card-content">
            <h3 class="card-title">최신 여행</h3>
            <p class="card-desc">새로 나온 여행 상품 모음</p>
          </div>
        </div>

        <div class="category-card" @click="goCategory('honeymoon')">
          <div class="card-icon">❤️</div>
          <div class="card-content">
            <h3 class="card-title">신혼 여행</h3>
            <p class="card-desc">로맨틱한 신혼여행 패키지</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const searchQuery = ref('')

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
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.home-wrapper {
  width: 100%;
  min-height: 100vh;
  background: #f8f8f8;
}

/* 네비게이션 */
.top-nav {
  background: white;
  border-bottom: 1px solid #e5e5e5;
  padding: 0;
}

.nav-buttons {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 20px;
}

.nav-btn {
  padding: 10px 28px;
  font-size: 16px;
  font-weight: 600;
  background: white;
  border: 2px solid #7c6bb5;
  border-radius: 24px;
  color: #7c6bb5;
  cursor: pointer;
  transition: all 0.3s;
}

.nav-btn:hover,
.nav-btn.active {
  background: #7c6bb5;
  color: white;
}

/* 히어로 섹션 */
.hero-section {
  background-image: url('https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=1920');
  background-size: cover;
  background-position: center;
  padding: 80px 20px;
  position: relative;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(160, 130, 200, 0.6);
}

.hero-content {
  position: relative;
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

.hero-title {
  font-size: 56px;
  font-weight: 700;
  color: white;
  margin-bottom: 40px;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
}

/* 검색 영역 */
.search-container {
  display: flex;
  max-width: 700px;
  margin: 0 auto 30px;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.search-input {
  flex: 1;
  padding: 18px 24px;
  font-size: 16px;
  border: none;
  outline: none;
  color: #333;
}

.search-input::placeholder {
  color: #aaa;
}

.search-btn {
  padding: 18px 40px;
  font-size: 16px;
  font-weight: 600;
  background: #5cb85c;
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
}

.search-btn:hover {
  background: #4cae4c;
}

/* 탭 버튼 */
.tab-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}

.tab-btn {
  padding: 12px 24px;
  font-size: 15px;
  font-weight: 500;
  background: rgba(255, 255, 255, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 24px;
  color: white;
  cursor: pointer;
  transition: all 0.3s;
  backdrop-filter: blur(8px);
}

.tab-btn:hover {
  background: rgba(255, 255, 255, 0.35);
  border-color: white;
}

/* 카테고리 섹션 */
.category-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 20px;
}

.section-title {
  font-size: 28px;
  font-weight: 700;
  color: #333;
  text-align: center;
  margin-bottom: 40px;
}

.category-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
}

@media (max-width: 768px) {
  .category-grid {
    grid-template-columns: 1fr;
  }
}

.category-card {
  background: white;
  border: 2px solid #e0e0e0;
  border-radius: 16px;
  padding: 40px 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s;
}

.category-card:hover {
  border-color: #7c6bb5;
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(124, 107, 181, 0.2);
}

.card-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.card-content {
  width: 100%;
}

.card-title {
  font-size: 22px;
  font-weight: 700;
  color: #333;
  margin-bottom: 12px;
}

.card-desc {
  font-size: 15px;
  color: #666;
  line-height: 1.5;
}
</style>
