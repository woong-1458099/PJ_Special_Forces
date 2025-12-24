<template>
  <header class="header">
    <nav class="nav">
      <RouterLink to="/concept" class="nav-btn" active-class="active">컨셉</RouterLink>
      <RouterLink to="/places" class="nav-btn" active-class="active">추천</RouterLink>
      <RouterLink to="/packages" class="nav-btn" active-class="active">코스</RouterLink>
      <RouterLink to="/mypage" class="nav-btn" active-class="active">마이</RouterLink>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.header{
  border-bottom: 2px solid var(--border);
  background: white;
}
.nav{
  max-width: var(--maxw);
  margin: 0 auto;
  padding: 14px 20px;
  display:flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
}
.nav-btn{
  border: 2px solid var(--border);
  border-radius: 999px;
  padding: 10px 14px;
  font-weight: 900;
  color: var(--purple);
  background: white;
}
.nav-btn:hover{
  background: var(--purple-2);
}
.active{
  background: var(--purple);
  color: white;
}
</style>
