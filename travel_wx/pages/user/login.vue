<template>
	<view class="container">
		<!-- 旅行logo -->
		<image class="logo" src="@/static/favicon.png"></image>
		<!-- 用户名密码登录 -->
		<view class="main_login">
			<uni-forms ref="loginRef" :rules="rules" :model="loginForm">
				<uni-forms-item name="username">
					<uni-easyinput :styles="inputStyle" prefix-icon="person" type="text" v-model="loginForm.username" placeholder="请输入用户名或者邮箱" />
				</uni-forms-item>
				<uni-forms-item name="password">
					<uni-easyinput :styles="inputStyle" prefix-icon="locked" type="password" v-model="loginForm.password" placeholder="请输入密码" />
				</uni-forms-item>
			</uni-forms>
			<button type="default" @click="clickLogin">登录</button>
		</view>
		<!-- 微信授权登录 -->
	    <button class="confirm-btn" open-type="getUserInfo" @click="wxLogin">微信授权登录</button>
	</view>
</template>

<script>
	import urls from '../../store/index.js'
	import { mapMutations } from 'vuex';
	
	export default{
		data(){
			return {
				// 微信登录输入表单
				wxLoginForm:{
					code:"",
					user_info: ""
				},
				// 登录输入表单
				loginForm:{
					username:"",
					password:""
				},
				// 校验规则
				rules: {
					username: {
						rules: [{
							required: true,
							errorMessage: '用户名不能为空'
						}]
					},
					password: {
						rules: [{
							required: true,
							errorMessage: '密码不能为空'
						}]
					}
				},
				// 输入框样式
				inputStyle:{
					color: 'black',
					borderColor: '#87CEEB'
				}
			}
		},
		onLoad() {},
		methods: {
			...mapMutations(['saveLoginStatus','saveUserInfo']),
			// 微信登录
			wxLogin(e) {
				let userInfo = e.detail.userInfo;
				uni.login({
					provider:"weixin",
					success:(login_res => {
						this.wxLoginForm.code = login_res.code
						uni.getUserInfo({
							provider: 'weixin',
							success:(async(info_res) => {
								this.wxLoginForm.user_info = info_res.rawData
								const response = await this.$api.user.wxLogin(this.wxLoginForm)
								if(response.statusCode===200)
								{
									console.log(' 登录成功')
									// 提示登录成功
									uni.showToast({
										title: '登陆成功',
										duration: 1000
									})
									// console.log('登录成功')
									//保存用户登录状态
									this.saveLoginStatus(response.data)
									// 获取用户信息
									this.getUserInfo(response.data.user.id)
									// 页面跳转
									// 获取当前页面栈（历史访问的路由信息）数量
									const res = getCurrentPages()
									// 判断历史路由是否大于1
									if(res.length <= 1){
										// 跳转到用户中心页面
										uni.switchTab({
											url:'/pages/user/user'
										})
									}else{
										// 返回上一级页面
										uni.navigateBack()
									}
								}
							})
						})
						
					})
				})
			},
			// 账号密码登录
			clickLogin(){
				// 点击登录校验请求参数
				this.$refs.loginRef.validate().then(res=>{
					// 调用登录方法
					this.submitLogin();
				}).catch(err =>{
					console.log('表单错误信息：', err);
				})
			},
			// 发送登录请求接口
			async submitLogin(){
				const response =  await this.$api.user.login(this.loginForm)
				if(response.statusCode===200){
					// 提示登录成功
					uni.showToast({
						title: '登陆成功',
						duration: 1000
					})
					// console.log('登录成功')
					//保存用户登录状态
					this.saveLoginStatus(response.data)
					// 获取用户信息
					this.getUserInfo(response.data.id)
					// 页面跳转
					// 获取当前页面栈（历史访问的路由信息）数量
					const res = getCurrentPages()
					// 判断历史路由是否大于1
					if(res.length <= 1){
						// 跳转到用户中心页面
						uni.switchTab({
							url:'/pages/user/user'
						})
					}else{
						// 返回上一级页面
						uni.navigateBack()
					}
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
		width: 100%;
		height: 100%;
	}
	// 旅行logo样式
	.logo{
		width: 200upx;
		height: 200upx;
		display: block;
		margin: 0 auto;
		margin-top: 30%;
	}
	// 用户名密码登录样式
	.main_login{
		margin: 0 50upx;
		margin-top: 30upx;
		button{
			border-radius: 40upx;
			background-color: $uni-primary;
			color:white
		}
	}
	// 微信授权登录样式
	.confirm-btn{
		margin: 30upx 50upx;
		border-radius: 40upx;
		background-color: $uni-primary;
		color: white;
	}
</style>