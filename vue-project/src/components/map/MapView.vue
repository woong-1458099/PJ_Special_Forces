<template>
  <div class="map-container">
    <div id="map" class="map"></div>
    <div v-if="selectedPlace" class="place-info-card">
      <h3>{{ selectedPlace.name }}</h3>
      <p>{{ selectedPlace.address }}</p>
      <p>{{ selectedPlace.category }}</p>
      <p v-if="selectedPlace.average_price">평균 가격: {{ selectedPlace.average_price }}원</p>
      <button @click="viewDetails(selectedPlace.id)">상세 보기</button>
      <button @click="selectedPlace = null">닫기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MapView',
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
      selectedPlace: null
    }
  },
  mounted() {
    this.initMap()
  },
  watch: {
    places() {
      this.updateMarkers()
    }
  },
  methods: {
    initMap() {
      // Google Maps 또는 Kakao Maps 초기화
      // 여기서는 기본 HTML5 Geolocation 사용
      console.log('지도 초기화:', this.center)

      // TODO: 실제 지도 API 연동
      // 예: Kakao Maps, Google Maps, Naver Maps

      // 임시 메시지
      this.loadExternalMapAPI()
    },

    loadExternalMapAPI() {
      // Kakao Maps 로드 예시 (실제 사용 시 활성화)
      /*
      const script = document.createElement('script')
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=YOUR_KAKAO_API_KEY&autoload=false`
      script.onload = () => {
        window.kakao.maps.load(() => {
          this.createKakaoMap()
        })
      }
      document.head.appendChild(script)
      */
    },

    createKakaoMap() {
      // Kakao Map 생성
      /*
      const container = document.getElementById('map')
      const options = {
        center: new kakao.maps.LatLng(this.center.lat, this.center.lng),
        level: 3
      }
      this.map = new kakao.maps.Map(container, options)
      this.updateMarkers()
      */
    },

    updateMarkers() {
      // 기존 마커 제거
      this.markers.forEach(marker => marker.setMap(null))
      this.markers = []

      // 새 마커 추가
      this.places.forEach(place => {
        if (place.latitude && place.longitude) {
          this.addMarker(place)
        }
      })
    },

    addMarker(place) {
      // 마커 추가 (Kakao Maps 예시)
      /*
      const position = new kakao.maps.LatLng(place.latitude, place.longitude)
      const marker = new kakao.maps.Marker({
        position: position,
        map: this.map
      })

      kakao.maps.event.addListener(marker, 'click', () => {
        this.selectedPlace = place
      })

      this.markers.push(marker)
      */

      console.log('마커 추가:', place.name, place.latitude, place.longitude)
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
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.map::before {
  content: '🗺️ 지도 컴포넌트 (Kakao/Google Maps API 연동 필요)';
  font-size: 18px;
  color: #666;
}

.place-info-card {
  position: absolute;
  top: 20px;
  right: 20px;
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  max-width: 300px;
  z-index: 1000;
}

.place-info-card h3 {
  margin-top: 0;
  margin-bottom: 10px;
  font-size: 20px;
}

.place-info-card p {
  margin: 8px 0;
  color: #666;
}

.place-info-card button {
  margin-right: 10px;
  margin-top: 10px;
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  background: #4CAF50;
  color: white;
}

.place-info-card button:last-child {
  background: #999;
}
</style>
