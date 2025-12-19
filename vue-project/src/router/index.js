import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

import Home from '@/views/Home.vue'
import ConceptSelect from '@/views/ConceptSelect.vue'
import Explore from '@/views/Explore.vue'
import PlaceDetail from '@/views/PlaceDetail.vue'
import PackageNew from '@/views/PackageNew.vue'
import MyPage from '@/views/MyPage.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import NotFound from '@/views/NotFound.vue'

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/concept', name: 'concept', component: ConceptSelect },
  { path: '/explore', name: 'explore', component: Explore },
  { path: '/places/:id', name: 'placeDetail', component: PlaceDetail, props: true },

  
  { path: '/packages/new', name: 'packageNew', component: PackageNew, meta: { requiresAuth: true } },
  { path: '/mypage', name: 'mypage', component: MyPage, meta: { requiresAuth: true } },

  { path: '/login', name: 'login', component: Login },
  { path: '/signup', name: 'signup', component: Signup },

  { path: '/:pathMatch(.*)*', name: 'notfound', component: NotFound },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth && !auth.isLoggedIn) {
    return { name: 'login', query: { next: to.fullPath } }
  }
})

export default router
