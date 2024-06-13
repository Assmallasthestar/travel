<template>
	<view class="container">
		<uni-forms ref="baseForm" :modelValue="baseFormData">
			<uni-forms-item>
				<uni-easyinput prefix-icon="email" v-model="formData.email" placeholder="请输入邮箱" />
			</uni-forms-item>
		</uni-forms>
		<button @click="saveemail">保存</button>
	</view>
</template>

<script>
	import { mapMutations, mapState } from 'vuex'
	export default{
		computed:{
			...mapState(['userInfo'])
		},
		onLoad() {
			this.formData.email = this.userInfo.email
		},
		data(){
			return{
				formData:{
					email:''
				}
			}
		},
		methods:{
			...mapMutations(['saveUserInfo']),
			// 保存昵称
			async saveemail(){
				const response = await this.$api.user.updateEmail(this.userInfo.id,this.formData)
				if(response.statusCode===200){
					uni.showToast({
						title:"修改成功！"
					})
					// 更新vuex中用户数据
					this.getUserInfo(this.userInfo.id)
				}
			},
			async getUserInfo(id){
				const response = await this.$api.user.getUserInfo(id)
				if(response.statusCode===200){
					//保存信息到vuex
					this.saveUserInfo(response.data)
				}
			}
		}
	}
</script>

<style scoped lang="scss">
	.container{
		margin: 40upx 10upx 20upx 10upx;
		
		button{
			color: white;
			background-color: $uni-primary;
		}
	}
</style>