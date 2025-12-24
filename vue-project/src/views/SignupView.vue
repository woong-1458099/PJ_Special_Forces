<template>
  <section>
    <h2>회원가입</h2>

    <form @submit.prevent="onSubmit" class="form">
      <input v-model="username" placeholder="username" />
      <input v-model="password" type="password" placeholder="password" />
      <button>가입</button>
    </form>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authAPI } from '@/api/auth'

const router = useRouter()
const username = ref('')
const password = ref('')

const onSubmit = async () => {
  try {
    await authAPI.signup({ username: username.value, password: password.value })
    router.push('/login')
  } catch (e) {
    alert('백엔드 연결 전이라 회원가입은 임시입니다.')
    router.push('/login')
  }
}
</script>

<style scoped>
.form { display:grid; gap:8px; max-width: 320px; }
</style>
