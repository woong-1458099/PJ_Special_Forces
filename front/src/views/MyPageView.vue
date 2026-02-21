<template>
  <section>
    <h2>마이페이지</h2>

    <div v-if="!auth.isLogin">
      <p>로그인이 필요합니다.</p>
      <button @click="$router.push('/login')">로그인</button>
    </div>

    <div v-else>
      <p>사용자: {{ auth.user?.username || '로딩중' }}</p>
      <button @click="auth.logout()">로그아웃</button>

      <hr />

      <h3>저장된 여행 코스</h3>
      <button @click="load">불러오기</button>
      <ul>
        <li v-for="p in packages.mine" :key="p.id">
          {{ p.title || p.id }}
          <button @click="packages.remove(p.id)">삭제</button>
        </li>
      </ul>

      <hr />

      <h3>선호 컨셉(임시)</h3>
      <p>{{ places.concept || '미설정' }}</p>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { usePackagesStore } from '@/stores/packages'
import { usePlacesStore } from '@/stores/places'

const auth = useAuthStore()
const packages = usePackagesStore()
const places = usePlacesStore()

const load = async () => {
  try {
    await packages.fetchMine()
  } catch (e) {
    packages.mine = [{ id: 1, title: '샘플 저장 코스' }]
  }
}

onMounted(async () => {
  if (auth.isLogin && !auth.user) {
    try { await auth.fetchMe() } catch (e) {}
  }
})
</script>
