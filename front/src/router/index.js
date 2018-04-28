import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import upload from '@/components/upload'
import post from '@/components/post'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/upload',
      name: 'upload',
      component: upload
    },
    {
      path: '/post',
      name: 'post',
      component: post
    }
  ]
})
