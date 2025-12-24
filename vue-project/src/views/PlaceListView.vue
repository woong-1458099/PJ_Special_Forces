<template>
  <section class="container">
    <h2 class="page-title">추천 장소</h2>
    <p class="subtitle">선택 컨셉: <b>{{ places.concept || '미선택' }}</b></p>

    <!-- 필터 및 정렬 바 -->
    <div class="filter-bar">
      <select v-model="sort" @change="onChangeSort" class="select-input">
        <option value="rating">평점순</option>
        <option value="distance">거리순</option>
        <option value="price">가격순</option>
      </select>

      <button @click="toggleMapView" class="map-toggle-btn">
        {{ showMap ? '목록 보기' : '지도 보기' }}
      </button>

      <button @click="refresh" class="refresh-btn">새로고침</button>
    </div>

    <!-- 지도 뷰 -->
    <div v-if="showMap" class="map-section">
      <MapView :places="places.list" />
    </div>

    <!-- 로딩 상태 -->
    <div v-if="loading" class="loading">
      <div class="spinner"></div>
      <p>불러오는 중...</p>
    </div>

    <!-- 장소 목록 -->
    <div v-else-if="!showMap" class="places-grid">
      <article
        v-for="p in places.list"
        :key="p.id"
        class="place-card"
        @click="goDetail(p.id)"
      >
        <div v-if="p.image_url" class="card-image" :style="{ backgroundImage: `url(${p.image_url})` }"></div>
        <div v-else class="card-image-placeholder">📷</div>

        <div class="card-content">
          <h3 class="card-title">{{ p.name }}</h3>
          <p class="card-category">{{ getCategoryLabel(p.category) }}</p>
          <p class="card-address">{{ p.address }}</p>

          <div class="card-footer">
            <span class="rating">⭐ {{ p.rating || '0.0' }}</span>
            <span v-if="p.average_price" class="price">{{ formatPrice(p.average_price) }}</span>
          </div>
        </div>
      </article>

      <div v-if="places.list.length === 0" class="empty-state">
        <p>추천 장소가 없습니다.</p>
        <button @click="refresh">다시 시도</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { usePlacesStore } from '@/stores/places'
import MapView from '@/components/map/MapView.vue'

const router = useRouter()
const places = usePlacesStore()

const loading = ref(false)
const sort = ref(places.sort)
const showMap = ref(false)

const onChangeSort = () => {
  places.setSort(sort.value)
  refresh()
}

const toggleMapView = () => {
  showMap.value = !showMap.value
}

const refresh = async () => {
  loading.value = true
  try {
    await places.fetchRecommend()
  } catch (e) {
    // 백엔드 없을 때도 화면이 죽지 않게
    places.list = [
      { id: 1, name: '샘플 장소 A', category: 'tourist', address: '서울시', rating: 4.6, average_price: 30000 },
      { id: 2, name: '샘플 장소 B', category: 'restaurant', address: '부산시', rating: 4.2, average_price: 15000 },
    ]
  } finally {
    loading.value = false
  }
}

const getCategoryLabel = (category) => {
  const labels = {
    tourist: '관광지',
    restaurant: '맛집',
    hotel: '숙박',
    activity: '액티비티',
    shopping: '쇼핑'
  }
  return labels[category] || category
}

const formatPrice = (price) => {
  return `${(price / 10000).toFixed(1)}만원`
}

const goDetail = (id) => router.push(`/places/${id}`)

onMounted(refresh)
</script>

<style scoped>
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 20px;
}

.page-title {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 8px;
  color: #2c3e50;
}

.subtitle {
  font-size: 16px;
  color: #7f8c8d;
  margin-bottom: 24px;
}

.filter-bar {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-bottom: 24px;
}

.select-input {
  padding: 10px 16px;
  font-size: 14px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  background: white;
}

.map-toggle-btn,
.refresh-btn {
  padding: 10px 20px;
  font-size: 14px;
  font-weight: 600;
  border: 2px solid #4CAF50;
  border-radius: 8px;
  cursor: pointer;
  background: white;
  color: #4CAF50;
  transition: all 0.2s ease;
}

.map-toggle-btn:hover,
.refresh-btn:hover {
  background: #4CAF50;
  color: white;
}

.map-section {
  margin-bottom: 40px;
}

.loading {
  text-align: center;
  padding: 60px 20px;
}

.spinner {
  width: 50px;
  height: 50px;
  margin: 0 auto 20px;
  border: 4px solid #e0e0e0;
  border-top: 4px solid #4CAF50;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.places-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
}

.place-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
}

.place-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  border-color: #4CAF50;
}

.card-image {
  width: 100%;
  height: 200px;
  background-size: cover;
  background-position: center;
}

.card-image-placeholder {
  width: 100%;
  height: 200px;
  background: #f5f5f5;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 60px;
}

.card-content {
  padding: 20px;
}

.card-title {
  font-size: 20px;
  font-weight: 600;
  margin: 0 0 8px 0;
  color: #2c3e50;
}

.card-category {
  font-size: 14px;
  color: #4CAF50;
  font-weight: 600;
  margin: 4px 0;
}

.card-address {
  font-size: 14px;
  color: #7f8c8d;
  margin: 8px 0;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #e0e0e0;
}

.rating {
  font-size: 16px;
  font-weight: 600;
  color: #f39c12;
}

.price {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
}

.empty-state {
  grid-column: 1 / -1;
  text-align: center;
  padding: 60px 20px;
  color: #7f8c8d;
}

.empty-state button {
  margin-top: 20px;
  padding: 12px 24px;
  font-size: 16px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
</style>
