import { createRouter, createWebHistory } from 'vue-router'
import NationView from '../views/NationInfoView.vue'
import ProView from '../views/ProInfoView.vue'
import ElseView from '../views/ElseInfoView.vue'
import HomePage from '../views/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/nation',
    name: 'nation_info',
    component: NationView
  },
  {
    path: '/pro',
    name: 'pro_info',
    component: ProView
  },
  {
    path: '/else',
    name: 'else_info',
    component: ElseView
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
