<template>
	<view class="container">
		<uni-forms ref="baseForm" :modelValue="baseFormData">
			<uni-forms-item>
				<uni-easyinput type="password" v-model="formData.password" prefix-icon="locked" placeholder="请输入新密码" />
			</uni-forms-item>
		</uni-forms>
		<uni-forms ref="baseForm" :modelValue="baseFormData">
			<uni-forms-item>
				<uni-easyinput type="password" v-model="formData.password_confirmation" prefix-icon="locked-filled" placeholder="请再次输入新密码" />
			</uni-forms-item>
		</uni-forms>
		<button @click="savepassword">保存</button>
	</view>
</template>

<script>
	import { mapMutations, mapState } from 'vuex'
	export default{
		computed:{
			...mapState(['userInfo'])
		},
		data(){
			return{
				formData:{
					password:'',
					password_confirmation:''
				}
			}
		},
		methods:{
			...mapMutations(['saveUserInfo']),
			// 保存昵称
			async savepassword(){
				const response = await this.$api.user.updatePassword(this.userInfo.id,this.formData)
				if(response.statusCode===200){
					uni.showToast({
						title:"修改成功！"
					})
					// 更新vuex中用户数据
					this.getUserInfo(this.userInfo.id)
					// uni.navigateBack()
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