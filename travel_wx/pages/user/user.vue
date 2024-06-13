<template>
    <view class="container">
		<!-- 手机状态栏 -->
		<view class="status_bar"></view>
		
		<!-- 顶部区域 -->
		<view class="top_bj">
			<!-- 用户头像 -->
			<!-- 登录显示头像 -->
			<view class="user-pic" v-if='isAuth'>
				<image :src="userInfo.avatar" class="user-icon" mode="aspectFit"></image>
			</view>
			<!-- 未登录显示图标 -->
			<view class="user-pic" v-else @click="navTo('/pages/user/login')">
				<image src="@/static/user/user_login.png" class="user-icon" mode="aspectFit"></image>
			</view>
			<!-- 用户信息 -->
			<!-- 登录显示昵称 -->
			<view class="user-info" v-if='isAuth'>
				{{userInfo.nick_name}}
			</view>
			<!-- 未登录显示用户名 -->
			<view @click="navTo('/pages/user/login')" v-else class="user-info">
				点击登录
			</view>
		</view>
		
		<!-- 弧形效果 -->
		<view class="camber"></view>
		
		<!-- 用户信息管理 -->
		<view class="menu-box">
			<uni-list>
				<uni-list-item clickable @click="navTo('/pages/user/my/myclloct')" :show-extra-icon="true" showArrow :extra-icon="Icon1" title="我的收藏"></uni-list-item>
				<uni-list-item clickable @click="navTo('/pages/user/my/mystrategy')" :show-extra-icon="true" showArrow :extra-icon="Icon2" title="我的攻略"></uni-list-item>
				<uni-list-item clickable @click="navTo('/pages/user/my/myrecommend')" :show-extra-icon="true" showArrow :extra-icon="Icon3" title="我的推荐"></uni-list-item>
				<uni-list-item clickable @click="navTo('/pages/user/set')" :show-extra-icon="true" showArrow :extra-icon="Icon4" title="个人设置"></uni-list-item>
				<uni-list-item clickable @click="navTo('/pages/user/feedback')" :show-extra-icon="true" showArrow :extra-icon="Icon5" title="问题反馈"></uni-list-item>
			</uni-list>
		</view>
    </view>
</template>
​
<script>
	import { mapState } from 'vuex'
	
	export default {
		data() {
			return {
				// 用户信息管理显示图标
				Icon1: {
					color: '#FFD700',
					size: '22',
					type: 'star-filled'
				},
				Icon2: {
					color: '#87CEEB',
					size: '22',
					type: 'map-filled'
				},
				Icon3: {
					color: '#4cd964',
					size: '22',
					type: 'hand-up-filled'
				},
				Icon4: {
					color: '#FA8072',
					size: '22',
					type: 'gear-filled'
				},
				Icon5: {
					color: '#EE82EE',
					size: '22',
					type: 'chat-filled',
				}
			}
		},
		computed: {
			...mapState(['isAuth','userInfo'])
		},
		methods: {
			navTo(url){
				if(this.isAuth){
					// console.log(url)
					uni.navigateTo({
						url: url
					})
				}else{
					uni.navigateTo({
						url: '/pages/user/login'
					})
				}
			}
		}
	};
</script>

<style scoped lang="scss">
	// 手机状态栏样式
	.status_bar{
		height: var(--status-bar-height);
		background-color: $uni-primary;
		width: 100%;
	}
	// 顶部区域样式
	.top_bj{
		height: 400upx;
		background-color: $uni-primary;
		display: flex;
		align-items: center;
		.user-pic{
			width: 150upx;
			height: 150upx;
			border-radius: 50%;
			background-color: #F0F8FF;
			margin: 0 50upx;
			line-height: 150upx;
			text-align: center;
			overflow: hidden;
			.user-icon{
				width: 150upx;
				height: 150upx;
			}
		}
		.user-info{
			flex: 1;
			color: #fff;
			font-size: 35upx;
		}
	}
	// 弧形效果样式
	.camber{
		height: 100upx;
		margin-top: -50upx;
		background-color: $uni-primary;
		border-radius: 0 0 50% 50%;
		margin-bottom: 30upx;
	}
	// 操作菜单列表样式
	.menu-box{
		background-color: #fff;
		margin: 5upx 20upx;
	}
</style>