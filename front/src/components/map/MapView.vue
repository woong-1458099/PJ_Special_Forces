<template>
  <div class="map-container">
    <!-- API 키 누락 안내 -->
    <div v-if="!hasApiKey" class="api-key-warning">
      <div class="warning-icon">🗺️</div>
      <h3>Google Maps API 키가 필요합니다</h3>
      <p>지도를 표시하려면 API 키를 설정해주세요</p>
      <ol class="setup-steps">
        <li>Google Cloud Console에서 API 키 발급</li>
        <li><code>front/.env</code> 파일 열기</li>
        <li><code>VITE_GOOGLE_MAPS_API_KEY=발급받은키</code> 입력</li>
        <li>개발 서버 재시작</li>
      </ol>
      <a href="https://console.cloud.google.com" target="_blank" class="btn-get-key">
        API 키 발급하기 →
      </a>
    </div>

    <!-- 지도 영역 -->
    <div v-else id="map" ref="mapElement" class="map"></div>

    <!-- 선택된 장소 정보 카드 -->
    <div v-if="selectedPlace && hasApiKey" class="place-info-card">
      <button @click="selectedPlace = null" class="close-btn">✕</button>
      <h3>{{ selectedPlace.name }}</h3>
      <p class="address">📍 {{ selectedPlace.address }}</p>
      <span class="category-badge">{{ getCategoryLabel(selectedPlace.category) }}</span>
      <div class="info-row">
        <span v-if="selectedPlace.rating" class="rating">
          ⭐ {{ selectedPlace.rating }}
        </span>
        <span v-if="selectedPlace.average_price" class="price">
          {{ formatPrice(selectedPlace.average_price) }}
        </span>
      </div>
      <button @click="viewDetails(selectedPlace.id)" class="btn-primary">상세 보기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MapView',
  emits: ['place-selected'],
  props: {
    places: {
      type: Array,
      default: () => []
    },
    center: {
      type: Object,
      default: () => ({ lat: 37.5665, lng: 126.9780 })
    }
  },
  data() {
    return {
      map: null,
      markers: [],
      selectedPlace: null,
      google: null,
      hasApiKey: false
    }
  },
  mounted() {
    this.checkApiKey()
    if (this.hasApiKey) {
      this.loadGoogleMaps()
    }
  },
  watch: {
    places: {
      handler() {
        if (this.map) {
          this.updateMarkers()
        }
      },
      deep: true
    }
  },
  methods: {
    checkApiKey() {
      const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY
      this.hasApiKey = apiKey && apiKey !== 'your-google-maps-api-key-here'
    },

    loadGoogleMaps() {
      const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY

      if (window.google && window.google.maps) {
        this.google = window.google
        this.initMap()
        return
      }

      const script = document.createElement('script')
      script.src = `https://maps.googleapis.com/maps/api/js?key=${apiKey}&libraries=places`
      script.async = true
      script.defer = true
      script.onload = () => {
        this.google = window.google
        this.initMap()
      }
      script.onerror = () => {
        console.error('Google Maps 로드 실패')
      }
      document.head.appendChild(script)
    },

    initMap() {
      if (!this.$refs.mapElement) return

      this.map = new this.google.maps.Map(this.$refs.mapElement, {
        center: this.center,
        zoom: 12,
        styles: [
          { featureType: 'poi', elementType: 'labels', stylers: [{ visibility: 'off' }] }
        ],
        mapTypeControl: false,
        fullscreenControl: false
      })

      this.updateMarkers()
    },

    updateMarkers() {
      if (!this.map) return

      this.markers.forEach(marker => marker.setMap(null))
      this.markers = []

      this.places.forEach(place => {
        if (place.latitude && place.longitude) {
          this.addMarker(place)
        }
      })

      if (this.markers.length > 0) {
        const bounds = new this.google.maps.LatLngBounds()
        this.markers.forEach(marker => bounds.extend(marker.getPosition()))
        this.map.fitBounds(bounds)
      }
    },

    addMarker(place) {
      const position = { lat: parseFloat(place.latitude), lng: parseFloat(place.longitude) }

      const markerColors = {
        tourist: '#FF6B6B',
        restaurant: '#4ECDC4',
        hotel: '#45B7D1',
        activity: '#FFA07A',
        shopping: '#98D8C8'
      }

      const marker = new this.google.maps.Marker({
        position,
        map: this.map,
        title: place.name,
        icon: {
          path: this.google.maps.SymbolPath.CIRCLE,
          scale: 10,
          fillColor: markerColors[place.category] || '#4CAF50',
          fillOpacity: 0.9,
          strokeColor: '#ffffff',
          strokeWeight: 2
        }
      })

      marker.addListener('click', () => {
        this.selectedPlace = place
        this.map.panTo(position)
        this.$emit('place-selected', place)
      })

      this.markers.push(marker)
    },

    getCategoryLabel(category) {
      const labels = {
        tourist: '관광지',
        restaurant: '맛집',
        hotel: '숙박',
        activity: '액티비티',
        shopping: '쇼핑'
      }
      return labels[category] || category
    },

    formatPrice(price) {
      return `${(price / 10000).toFixed(1)}만원`
    },

    viewDetails(placeId) {
      this.$router.push(`/places/${placeId}`)
    }
  }
}
</script>

<style scoped>
.map-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.map {
  width: 100%;
  height: 100%;
  border-radius: 12px;
  overflow: hidden;
}

/* API 키 경고 */
.api-key-warning {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  color: white;
  text-align: center;
}

.warning-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.api-key-warning h3 {
  font-size: 24px;
  margin: 0 0 12px 0;
}

.api-key-warning p {
  font-size: 16px;
  margin-bottom: 24px;
  opacity: 0.9;
}

.setup-steps {
  text-align: left;
  background: rgba(255,255,255,0.1);
  padding: 20px 20px 20px 40px;
  border-radius: 8px;
  margin-bottom: 24px;
  backdrop-filter: blur(10px);
}

.setup-steps li {
  margin: 8px 0;
  line-height: 1.6;
}

.setup-steps code {
  background: rgba(0,0,0,0.2);
  padding: 2px 8px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 14px;
}

.btn-get-key {
  display: inline-block;
  padding: 12px 32px;
  background: white;
  color: #667eea;
  text-decoration: none;
  border-radius: 50px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-get-key:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

/* 장소 정보 카드 */
.place-info-card {
  position: absolute;
  top: 20px;
  right: 20px;
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
  max-width: 300px;
  z-index: 1000;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.close-btn {
  position: absolute;
  top: 12px;
  right: 12px;
  background: none;
  border: none;
  font-size: 20px;
  color: #999;
  cursor: pointer;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.close-btn:hover {
  background: #f0f0f0;
  color: #333;
}

.place-info-card h3 {
  margin: 0 0 8px 0;
  font-size: 20px;
  font-weight: 600;
  color: #2c3e50;
  padding-right: 24px;
}

.address {
  font-size: 14px;
  color: #666;
  margin: 8px 0 12px 0;
  line-height: 1.4;
}

.category-badge {
  display: inline-block;
  padding: 4px 12px;
  background: #4CAF50;
  color: white;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.info-row {
  display: flex;
  gap: 12px;
  margin: 12px 0;
  padding-top: 12px;
  border-top: 1px solid #eee;
}

.rating, .price {
  font-size: 14px;
  font-weight: 600;
  color: #2c3e50;
}

.btn-primary {
  width: 100%;
  padding: 10px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 12px;
  transition: all 0.2s ease;
}

.btn-primary:hover {
  background: #45a049;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(76,175,80,0.3);
}
</style>
