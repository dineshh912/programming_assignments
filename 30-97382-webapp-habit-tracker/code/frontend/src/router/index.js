import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Register from "@/views/Register.vue"
import Login from "@/views/Login.vue"
import MentalHealth from "@/views/mh.vue"
import Diet from "@/views/Diet.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: 'Register',
    component: Register

  },
  {
    path: '/login',
    name: 'Login',
    component: Login

  },
  {
    path: '/mh',
    name: 'Mental Health',
    component: MentalHealth,
    meta: {requiresAuth: true},
  },
  {
    path: '/diet',
    name: 'Diet',
    component: Diet,
    meta: {requiresAuth: true},
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
