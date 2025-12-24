<template>
  <div class="map-container">
    <div id="map" ref="mapElement" class="map"></div>
    <div v-if="selectedPlace" class="place-info-card">
      <h3>{{ selectedPlace.name }}</h3>
      <p>{{ selectedPlace.address }}</p>
      <p class="category-badge">{{ getCategoryLabel(selectedPlace.category) }}</p>
      <p v-if="selectedPlace.average_price" class="price-info">
        💰 평균 가격: {{ formatPrice(selectedPlace.average_price) }}
      </p>
      <p v-if="selectedPlace.rating" class="rating-info">
        ⭐ 평점: {{ selectedPlace.rating }}
      </p>
      <div class="button-group">
        <button @click="viewDetails(selectedPlace.id)" class="btn-primary">상세 보기</button>
        <button @click="selectedPlace = null" class="btn-secondary">닫기</button>
      </div>
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
      default: () => ({ lat: 37.5665, lng: 126.9780 }) // 서울 기본 위치
    }
  },
  data() {
    return {
      map: null,
      markers: [],
      selectedPlace: null,
      google: null
    }
  },
  mounted() {
    this.loadGoogleMaps()
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
    loadGoogleMaps() {
      // Google Maps API 키 확인
      const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY

      if (!apiKey) {
        console.warn('Google Maps API 키가 없습니다. .env 파일에 VITE_GOOGLE_MAPS_API_KEY를 설정하세요.')
        this.showPlaceholder()
        return
      }

      // 이미 로드된 경우
      if (window.google && window.google.maps) {
        this.initMap()
        return
      }

      // Google Maps 스크립트 로드
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
        this.showPlaceholder()
      }
      document.head.appendChild(script)
    },

    initMap() {
      if (!this.$refs.mapElement) return

      // Google Map 생성
      this.map = new this.google.maps.Map(this.$refs.mapElement, {
        center: this.center,
        zoom: 13,
        styles: [
          {
            featureType: 'poi',
            elementType: 'labels',
            stylers: [{ visibility: 'off' }]
          }
        ]
      })

      // 초기 마커 추가
      this.updateMarkers()
    },

    updateMarkers() {
      if (!this.map) return

      // 기존 마커 제거
      this.markers.forEach(marker => marker.setMap(null))
      this.markers = []

      // 새 마커 추가
      this.places.forEach(place => {
        if (place.latitude && place.longitude) {
          this.addMarker(place)
        }
      })

      // 모든 마커가 보이도록 지도 영역 조정
      if (this.markers.length > 0) {
        const bounds = new this.google.maps.LatLngBounds()
        this.markers.forEach(marker => {
          bounds.extend(marker.getPosition())
        })
        this.map.fitBounds(bounds)
      }
    },

    addMarker(place) {
      const position = { lat: parseFloat(place.latitude), lng: parseFloat(place.longitude) }

      // 카테고리별 마커 색상
      const markerColors = {
        tourist: '#FF6B6B',
        restaurant: '#4ECDC4',
        hotel: '#45B7D1',
        activity: '#FFA07A',
        shopping: '#98D8C8'
      }

      const marker = new this.google.maps.Marker({
        position: position,
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

      // 마커 클릭 이벤트
      marker.addListener('click', () => {
        this.selectedPlace = place
        this.map.panTo(position)
        this.$emit('place-selected', place)
      })

      this.markers.push(marker)
    },

    showPlaceholder() {
      // API 키가 없을 때 플레이스홀더 표시
      if (this.$refs.mapElement) {
        this.$refs.mapElement.innerHTML = `
          <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; color: #666;">
            <div style="font-size: 48px; margin-bottom: 16px;">🗺️</div>
            <div style="font-size: 18px; text-align: center;">
              Google Maps API 키를 설정하세요<br/>
              <small style="font-size: 14px; color: #999;">
                .env 파일에 VITE_GOOGLE_MAPS_API_KEY 추가
              </small>
            </div>
          </div>
        `
      }
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
  height: 600px;
}

.map {
  width: 100%;
  height: 100%;
  background: #e8e8e8;
  border-radius: 12px;
  overflow: hidden;
}

.place-info-card {
  position: absolute;
  top: 20px;
  right: 20px;
  background: white;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  max-width: 320px;
  z-index: 1000;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.place-info-card h3 {
  margin: 0 0 12px 0;
  font-size: 22px;
  font-weight: 600;
  color: #2c3e50;
}

.place-info-card p {
  margin: 8px 0;
  color: #666;
  font-size: 14px;
  line-height: 1.5;
}

.category-badge {
  display: inline-block;
  padding: 4px 12px;
  background: #4CAF50;
  color: white;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  margin: 8px 0;
}

.price-info,
.rating-info {
  font-weight: 600;
  color: #2c3e50;
}

.button-group {
  display: flex;
  gap: 8px;
  margin-top: 16px;
}

.button-group button {
  flex: 1;
  padding: 10px 16px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
}

.btn-primary {
  background: #4CAF50;
  color: white;
}

.btn-primary:hover {
  background: #45a049;
  transform: translateY(-1px);
}

.btn-secondary {
  background: #e0e0e0;
  color: #666;
}

.btn-secondary:hover {
  background: #d0d0d0;
}
</style>
