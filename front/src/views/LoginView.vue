<template>
  <div class="login-page">
    <div class="login-container">
      <div class="login-card">
        <!-- 로고 -->
        <div class="logo-icon">
          <div class="checkmark">✓</div>
        </div>

        <h2 class="login-title">로그인</h2>

        <!-- 로그인 폼 -->
        <form @submit.prevent="onSubmit" class="login-form">
          <div class="form-group">
            <label>이메일</label>
            <input
              v-model="username"
              type="email"
              placeholder="example@domain.com"
              class="form-input"
            />
          </div>

          <div class="form-group">
            <label>비밀번호</label>
            <input
              v-model="password"
              type="password"
              placeholder="············"
              class="form-input"
            />
          </div>

          <div class="form-footer">
            <a href="#" class="forgot-password">비밀번호 찾기</a>
          </div>

          <button type="submit" class="login-btn">로그인 하기</button>
        </form>

        <!-- 회원가입 링크 -->
        <div class="signup-link">
          회원이 아니신가요?
          <router-link to="/signup" class="signup-link-text">
            지금 바로 가입하기 >
          </router-link>
        </div>

        <!-- 하단 링크 -->
        <div class="footer-links">
          <span>Snow Travel을 처음 사용하시나요?</span>
          <a href="#">이용 방법 알아보기</a>
        </div>
      </div>
    </div>
  </div>
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
.login-page {
  min-height: 100vh;
  background-image: url('https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=1920');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.login-page::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(4px);
}

.login-container {
  position: relative;
  z-index: 1;
}

.login-card {
  background: white;
  border-radius: 16px;
  padding: 48px 40px;
  width: 100%;
  max-width: 420px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
}

/* 로고 아이콘 */
.logo-icon {
  display: flex;
  justify-content: center;
  margin-bottom: 24px;
}

.checkmark {
  width: 64px;
  height: 64px;
  background: #4A90E2;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 32px;
  font-weight: bold;
}

/* 제목 */
.login-title {
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  color: #333;
  margin-bottom: 32px;
}

/* 폼 */
.login-form {
  margin-bottom: 24px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #555;
  margin-bottom: 8px;
}

.form-input {
  width: 100%;
  padding: 12px 16px;
  font-size: 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  outline: none;
  transition: border-color 0.3s;
}

.form-input:focus {
  border-color: #4A90E2;
}

.form-input::placeholder {
  color: #aaa;
}

.form-footer {
  text-align: right;
  margin-bottom: 24px;
}

.forgot-password {
  font-size: 13px;
  color: #4A90E2;
  text-decoration: none;
}

.forgot-password:hover {
  text-decoration: underline;
}

/* 로그인 버튼 */
.login-btn {
  width: 100%;
  padding: 14px;
  font-size: 16px;
  font-weight: 600;
  color: white;
  background: #4A90E2;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s;
}

.login-btn:hover {
  background: #357ABD;
}

/* 회원가입 링크 */
.signup-link {
  text-align: center;
  font-size: 14px;
  color: #666;
  padding: 20px 0;
  border-top: 1px solid #eee;
}

.signup-link-text {
  color: #4A90E2;
  text-decoration: none;
  font-weight: 600;
  margin-left: 4px;
}

.signup-link-text:hover {
  text-decoration: underline;
}

/* 하단 링크 */
.footer-links {
  text-align: center;
  font-size: 12px;
  color: #999;
  margin-top: 20px;
}

.footer-links span {
  display: block;
  margin-bottom: 4px;
}

.footer-links a {
  color: #4A90E2;
  text-decoration: none;
}

.footer-links a:hover {
  text-decoration: underline;
}
</style>
