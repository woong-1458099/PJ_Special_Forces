<template>
  <section class="container">
    <h1 class="title-center">Trip Connection</h1>
    <p class="subtitle-center">컨셉을 선택하면 추천 장소와 여행 코스를 만들어줘요.</p>

    <div class="grid-categories">
      <div
        v-for="c in concepts"
        :key="c"
        class="category-card"
        @click="goConcept(c)"
      >
        {{ c }}
      </div>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { usePlacesStore } from '@/stores/places'

const router = useRouter()
const places = usePlacesStore()

const concepts = ['헬스', '힐링', '카페', '쇼핑', '맛집', '산책']

const goConcept = (c) => {
  // 컨셉 선택 저장하고 바로 추천 페이지로 이동(원하면 /concept로 보내도 됨)
  places.setConcept(c)
  router.push('/explore')
}
</script>
