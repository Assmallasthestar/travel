<template>
	<view class="container">
		<form @submit="savegender">
			<radio-group name="gender">
				<label>
					<view class="box">
						<radio value=0 :checked="userInfo.gender === 0" />
						<text>男</text>
					</view>
				</label>
				<label>
					<view class="box">
						<radio value=1 :checked="userInfo.gender === 1" />
						<text>女</text>
					</view>
				</label>
				<label>
					<view class="box">
						<radio value=2 :checked="userInfo.gender === 2" />
						<text>未知</text>
					</view>
				</label>
			</radio-group>
			<button class="submit" form-type="submit">保存</button>
		</form>
	</view>
</template>

<script>
	import { userInfo } from 'os'
	import { mapMutations, mapState} from 'vuex'
	export default {
		data() {
			return {
				formData:{}
			}
		},
		computed:{
			...mapState(['userInfo']),
		},
		methods:{
			...mapMutations(['saveUserInfo']),
			async savegender(e){
				this.formData = e.detail.value
				const response = await this.$api.user.updateGender(this.userInfo.id,this.formData)
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
	.box{
		height: 100upx;
		line-height: 100upx;
		border: 1upx solid 	#B0C4DE;
	}
	.submit{
		margin: 0 20upx;
		margin-top: 30upx;
		color: white;
		background-color: $uni-primary;
	}
</style>