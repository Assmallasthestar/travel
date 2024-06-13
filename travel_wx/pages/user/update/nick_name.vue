<template>
	<view class="container">
		<uni-forms ref="baseForm" :modelValue="baseFormData">
			<uni-forms-item>
				<uni-easyinput prefix-icon="person" v-model="formData.nick_name" placeholder="请输入昵称" />
			</uni-forms-item>
		</uni-forms>
		<button @click="savenick_name">保存</button>
	</view>
</template>

<script>
	import { mapMutations, mapState } from 'vuex'
	export default{
		computed:{
			...mapState(['userInfo'])
		},
		onLoad() {
			this.formData.nick_name = this.userInfo.nick_name
		},
		data(){
			return{
				formData:{
					nick_name:''
				}
			}
		},
		methods:{
			...mapMutations(['saveUserInfo']),
			// 保存昵称
			async savenick_name(){
				const response = await this.$api.user.updateNickName(this.userInfo.id,this.formData)
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