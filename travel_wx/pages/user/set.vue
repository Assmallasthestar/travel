<template>
	<view class="container">
		<!-- 用户基本信息 -->
		<uni-list>
			<uni-list-item title="头像">
				<template v-slot:footer>
					<view class="img-flex">
						<image class="slot-image" v-if="userInfo.avatar" :src="userInfo.avatar" mode="heightFix" @click="updateImg"></image>
						<image class="slot-image" v-else src="../../static/tabbar_icon/my_selected.png" mode="heightFix" @click="updateImg"></image>
					</view>
				</template>
			</uni-list-item>
			<uni-list-item  title="用户名" :rightText="userInfo.username"></uni-list-item>
			<uni-list-item  clickable @click="navTo('/pages/user/update/nick_name')" showArrow title="昵称" :rightText="userInfo.nick_name"></uni-list-item>
			<uni-list-item  clickable @click="navTo('/pages/user/update/email')" showArrow title="邮箱" :rightText="userInfo.email"></uni-list-item>
			<uni-list-item  clickable @click="navTo('/pages/user/update/gender')" showArrow title="性别" :rightText="gender"></uni-list-item>
			<uni-list-item  clickable @click="navTo('/pages/user/update/password')" showArrow title="密码"></uni-list-item>
		</uni-list>
		<!-- 版本号 -->
		<uni-list class="version">
			<uni-list-item  title="版本" rightText="1.0.0"></uni-list-item>
		</uni-list>
		<!-- 退出登录 -->
		<view class="version">
			<button @click="logOut" type="default">退出登录</button>
		</view>
	</view>
</template>

<script>
	import { userInfo } from 'os'
	import { mapMutations, mapState} from 'vuex'
	export default{
		methods:{
			...mapMutations(['logOut']),
			navTo(url){
				uni.navigateTo({
					url: url
				})
			},
			updateImg(){
				uni.chooseImage({
					count:1,
					success: async (chooseImageRes) => {
						//获取头像token的接口
						// const data = await this.$api.api.user.getImgToken();
						console.log(chooseImageRes.tempFilePaths)
						const tempFiles = chooseImageRes.tempFiles;
						uni.uploadFile({
							url: 'http://127.0.0.1:8000/api/users/1/avatar/upload',	// 上传地址
							file: tempFiles[0],
							name: 'file',
							formData: {
								token: this.token, //头像token，参考返回数据
								key: new Date().getTime()+".png" // 图片名，移动端可能不存在name，可修改为 key: new Date().getTime()+".png" 随机
							},
							success: (uploadFileRes) => {
								// console.log(uploadFileRes);是一个字符串
								const data = JSON.parse(uploadFileRes.data)
								// 上传头像接口（参数根据自己的来）
								this.$api.api.user.updateImg({
									"headPath": "http://qapxsiqga.bkt.clouddn.com/"+data.key,	// 图片最终的路径，http://qapxsiqga.bkt.clouddn.com/是七牛云空间地址
									"userId": userId
								}).then(res=>{
									console.log(res)
									this.avar = "http://qapxsiqga.bkt.clouddn.com/"+data.key	// 存入修改后的头像
									this.avarShow = true	// 显示修改后的头像
								})
							}
						})
					}
				})
			}
		},
		data(){
			return{
				imageStyles: {
					width: 32,
					height: 32,
				},
			}
		},
		computed:{
			...mapState(['userInfo', 'token']),
			gender(){
				if(this.userInfo.gender===0){
					return '男'
				}else if(this.userInfo.gender===1){
					return '女'
				}else if(this.userInfo.gender===2){
					return '未知'
				}
			}
		}
	}
</script>

<style scoped lang="scss">
	.img-flex{
		display: flex;
		flex-direction: row-reverse;
		.slot-image{
			height: 100%;
			width: 100%;
		}
	}
	.version{
		margin-top: 30upx;
	}
	button{
		background-color: $uni-primary;
		color: white;
	}
</style>