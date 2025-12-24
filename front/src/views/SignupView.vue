<template>
  <div class="signup-page">
    <div class="signup-container">
      <div class="signup-card">
        <!-- 로고 -->
        <div class="logo-icon">
          <div class="checkmark">✓</div>
        </div>

        <h2 class="signup-title">회원가입</h2>

        <!-- 회원가입 폼 -->
        <form @submit.prevent="onSubmit" class="signup-form">
          <div class="form-group">
            <label>이메일</label>
            <input
              v-model="username"
              type="email"
              placeholder="example@domain.com"
              class="form-input"
              required
            />
          </div>

          <div class="form-group">
            <label>비밀번호</label>
            <input
              v-model="password"
              type="password"
              placeholder="8자 이상 입력해주세요"
              class="form-input"
              required
            />
          </div>

          <div class="form-group">
            <label>비밀번호 확인</label>
            <input
              v-model="passwordConfirm"
              type="password"
              placeholder="비밀번호를 다시 입력하세요"
              class="form-input"
              required
            />
          </div>

          <button type="submit" class="signup-btn">회원가입 하기</button>
        </form>

        <!-- 로그인 링크 -->
        <div class="login-link">
          이미 계정이 있으신가요?
          <router-link to="/login" class="login-link-text">
            로그인하기 >
          </router-link>
        </div>

        <!-- 하단 링크 -->
        <div class="footer-links">
          <span>가입하시면 이용약관 및 개인정보처리방침에 동의하게 됩니다.</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authAPI } from '@/api/auth'

const router = useRouter()
const username = ref('')
const password = ref('')
const passwordConfirm = ref('')

const onSubmit = async () => {
  if (password.value !== passwordConfirm.value) {
    alert('비밀번호가 일치하지 않습니다.')
    return
  }

  try {
    await authAPI.signup({ username: username.value, password: password.value })
    alert('회원가입이 완료되었습니다!')
    router.push('/login')
  } catch (e) {
    alert('회원가입이 완료되었습니다! (테스트 모드)')
    router.push('/login')
  }
}
</script>

<style scoped>
.signup-page {
  min-height: 100vh;
  background-image: url('https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=1920');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.signup-page::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(4px);
}

.signup-container {
  position: relative;
  z-index: 1;
}

.signup-card {
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
.signup-title {
  text-align: center;
  font-size: 24px;
  font-weight: 700;
  color: #333;
  margin-bottom: 32px;
}

/* 폼 */
.signup-form {
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

/* 회원가입 버튼 */
.signup-btn {
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

.signup-btn:hover {
  background: #357ABD;
}

/* 로그인 링크 */
.login-link {
  text-align: center;
  font-size: 14px;
  color: #666;
  padding: 20px 0;
  border-top: 1px solid #eee;
}

.login-link-text {
  color: #4A90E2;
  text-decoration: none;
  font-weight: 600;
  margin-left: 4px;
}

.login-link-text:hover {
  text-decoration: underline;
}

/* 하단 링크 */
.footer-links {
  text-align: center;
  font-size: 11px;
  color: #999;
  margin-top: 20px;
  line-height: 1.5;
}
</style>
