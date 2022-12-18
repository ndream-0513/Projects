import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import RegisterView from '../views/RegisterView.vue'
import UserListView from '../views/UserListView.vue'
import UserProfileView from '../views/UserProfileView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/login/',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/404/',
    name: 'NotFound',
    component: NotFoundView
  },
  {
    path: '/register/',
    name: 'Register',
    component: RegisterView
  },
  {
    path: '/userlist/',
    name: 'UserList',
    component: UserListView
  },
  {
    path: '/userprofile/',
    name: 'UserProfile',
    component: UserProfileView
  },
  {
    path: '/:catchAll(.*)',
    redirect: "/404/"
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
