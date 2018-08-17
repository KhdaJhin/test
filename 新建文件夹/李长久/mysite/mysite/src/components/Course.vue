<template>
  <div class="course">
    <ul v-for='item in msg'>
    	<li>{{item.name}}
    		<div class="row">
			  <div v-for='price in item.pricepolicy' 
			  	class="col-md-4">
			  	<button type="button" 
			  			class="btn btn-default btn-lg"  
			  			v-on:click='gainprice(price.valid_period,item.name,item.id,price.price)'>
			  		{{price.price}}
			  	</button>
			  </div> <br> <br> <br>
			  <button type="button" 
			  		  class="btn btn-warning"
					  v-on:click='addcourse()'
			  		  >加入购物车</button>
			</div>
    </li>
    	
    </ul>
  </div>

</template>

<script>
export default {
  name: 'course',
  data () {
    return {
      msg:[{
      	'name':'python'},
      	{'name':'java'},
      	{'name':'c'}
      ],
      end_data:{'1':
      	{
      	'end_price':'',
      	'course_name':'',
      	'course_id':'',
      	'course_price':''
      		}
}
    }
  },
  // 加载的时候执行
  mounted(){
      this.initCourse();
      // this.testCors();
 	},
  methods:{
  		initCourse:function(){
  			var that=this
  			this.$axios.request({
  				url:'http://127.0.0.1:8008/api/v1/course/',
  				method:'GET',
  				responseType:'json'
  			}).then(function(arg){
  				console.log(arg)
  				if (arg.data.code === 1000){
  					that.msg=arg.data.data

  				}else {
  					console.log(arg.data.error)
  					
  				}
  			}).catch(function(arg){
  				console.log(arg)
  			})
  		},
  		// 获取价格
  		gainprice:function(valid_period,name,id,price){
  			// 将价格策略的周期获取到并给data中end_price赋值
  			this.end_data['1']['end_price']=valid_period;
  			this.end_data['1']['course_name']=name;
  			this.end_data['1']['course_id']=id;
  			this.end_data['1']['course_price']=price;
 			console.log(this.end_data);

  		},
  		//发送post请求
  		addcourse:function(){
  			var that=this
  			this.$axios.request({
  				url:'http://127.0.0.1:8008/api/v1/course/',
  				method:'POST',
  				responseType:'json',
  				data:this.end_data
  			}).then(function(arg){
  				alert(arg.data)

  				
  			}).catch(function(arg){
  				console.log(arg.data)
  			})

  		}
  }
}
</script>
<style scoped>

</style>
