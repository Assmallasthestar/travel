<script>
	import { mapMutations } from 'vuex'
	export default {
		methods:{
			...mapMutations(['saveLoginStatus', 'saveUserInfo'])
		},
		onLaunch: function() {
			//获取登录信息
			uni.getSetting({
			    success(res) {                    
					if (!res.authSetting['scope.userLocation']) {
					// 未授权
						 uni.authorize({
							 scope: 'scope.userLocation',
							 success() { // 允许授权
								  uni.getLocation()
								 
							 },
							 fail(){    // 拒绝授权
								 console.log("你拒绝了授权，无法获得周边信息")
							 }
						 })
					}else{
						 // 已授权 ..(获取位置信息)
					}
				}
			});
		},
		onShow: function() {
			// 解决刷新页面，vuex中用户信息丢失问题
			// 读取uni-appStorage中存储的用户信息，保存到vuex
			const uinfo = uni.getStorageSync('userinfo') || {}
			const loginStatus = {
				token: uni.getStorageSync('token'),
				refresh: uni.getStorageSync('refresh')
			}
			// 保存登录状态
			this.saveLoginStatus(loginStatus)
			// 保存用户信息
			this.saveUserInfo(uinfo)
		},
		onHide: function() {
			
		}
	}
</script>

<style lang="scss">
	/*每个页面公共css */
	@import '@/uni_modules/uni-scss/index.scss';
	/* #ifndef APP-NVUE */
	@import '@/static/customicons.css';
	// 设置整个项目的背景色
	page {
		background-color: #f5f5f5;
	}
	uni-page-body,html,body{  
	            height: 100%;  
	}
	/* #endif */
	.example-info {
		font-size: 14px;
		color: #333;
		padding: 10px;
	}
	// 引入iconfont
	@import url("./iconfont/iconfont.css")
</style>
