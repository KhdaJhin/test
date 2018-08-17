<template>
  <div id="app">
   <router-link to='/'>首页</router-link> 
   <router-link to='/course'>课程</router-link> 
   <router-link to='/login'>登录</router-link> 
    <router-view/>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
export default {
  name: 'App'
}
</script>

<style>
</style>
