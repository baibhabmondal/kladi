import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import upload from '@/components/upload'
import post from '@/components/post'
import post1 from '@/components/post1'


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
    },
      {
        path: '/post1',
        name: 'post1',
        component: post1
      }

  ]
})
