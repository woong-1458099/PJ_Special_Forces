import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

import HomeView from '@/views/HomeView.vue'
import ConceptView from '@/views/ConceptView.vue'
import PlaceListView from '@/views/PlaceListView.vue'
import PlaceDetailView from '@/views/PlaceDetailView.vue'
import PackageView from '@/views/PackageView.vue'
import MyPageView from '@/views/MyPageView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import SearchView from '@/views/SearchView.vue'
import NotFoundView from '@/views/NotFoundView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: HomeView },

    { path: '/concept', name: 'concept', component: ConceptView },
    { path: '/places', name: 'places', component: PlaceListView },
    { path: '/places/:id', name: 'placeDetail', component: PlaceDetailView, props: true },

    { path: '/packages', name: 'packages', component: PackageView },
    { path: '/mypage', name: 'mypage', component: MyPageView, meta: { requiresAuth: true } },

    { path: '/login', name: 'login', component: LoginView },
    { path: '/signup', name: 'signup', component: SignupView },

    { path: '/search', name: 'search', component: SearchView },

    { path: '/:pathMatch(.*)*', name: 'notfound', component: NotFoundView },
  ],
})

router.beforeEach((to) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth && !auth.isLogin) {
    return { name: 'login', query: { next: to.fullPath } }
  }
})

export default router
