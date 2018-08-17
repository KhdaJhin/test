<template>
  <div class="login">
      <input type="'text" name="name">
      <input type="'password" name="pwd">
      <button @click="tologin">提交</button> 
  </div>

</template>
<script>
export default {
  name: 'login',
  data () {
    return {
      msg:111
    }
  },
  // 加载的时候执行
  methods:{
  		tologin:function(){
  			var that=this
  			this.$axios.request({
  				url:'http://127.0.0.1:8008/api/v1/course/',
  				method:'POST',
          headers:{
                  'Content-Type:':'application/json',
                },
  				responseType:'json'
  			}).then(function(arg){
            console.log(arg)
  			}).catch(function(arg){
  				console.log(arg)
  			})



  		}
  }
}
</script>
<style scoped>

</style>
