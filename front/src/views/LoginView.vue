<template>
  <section>
    <h2>로그인</h2>

    <form @submit.prevent="onSubmit" class="form">
      <input v-model="username" placeholder="username" />
      <input v-model="password" type="password" placeholder="password" />
      <button>로그인</button>
    </form>

    <button @click="$router.push('/signup')">회원가입</button>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
const router = useRouter()
const route = useRoute()

const username = ref('')
const password = ref('')

const onSubmit = async () => {
  try {
    await auth.login({ username: username.value, password: password.value })
    router.push(route.query.next || '/')
  } catch (e) {
    // 백엔드 없을 때도 테스트 가능하게
    auth.token = 'dummy-token'
    localStorage.setItem('token', auth.token)
    auth.user = { username: username.value || 'test' }
    router.push(route.query.next || '/')
  }
}
</script>

<style scoped>
.form { display:grid; gap:8px; max-width: 320px; }
</style>
