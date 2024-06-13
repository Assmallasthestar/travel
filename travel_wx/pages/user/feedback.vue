<template>
	<view class="container">
		<uni-forms ref="baseForm" :modelValue="baseFormData">
			<uni-forms-item>
				<uni-easyinput type="textarea" autoHeight v-model="formData.content" placeholder="请输入所发现的问题" />
			</uni-forms-item>
		</uni-forms>
		<button @click="savefeedback">提交反馈</button>
	</view>
</template>

<script>
	import { mapState } from 'vuex'
	export default{
		computed:{
			...mapState(['userInfo'])
		},
		data(){
			return{
				formData:{
					user:'',
					content:''
				}
			}
		},
		methods:{
			async savefeedback(){
				this.formData.user = this.userInfo.id
				const response = await this.$api.user.createFeedback(this.formData)
				if(response.statusCode===201){
					uni.showToast({
						title:"反馈成功！",
					})
					uni.navigateBack()
				}
			},
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