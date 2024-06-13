<template>
	<view class="container">
		<!-- 攻略列表 -->
		<view class="strategy-item" v-for='s in strategy' :key='s.id' @click="toStrategyDetail(s.id)">
			<view class="left_img">
				<image v-if="s.img" class="recommend_img" :src="s.img" mode="heightFix"></image>
				<view v-else class="recommend_img">暂无图片</view>
			</view>
			<view class="middle_other">
				<view class="name">{{s.title}}</view>
				<view class="desc" v-if="s.desc">{{r.desc}}</view>
				<view class="desc" v-else>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import { mapState } from 'vuex'
	export default{
		data(){
			return{
				strategy: []
			}
		},
		computed: {
			...mapState(['isAuth','userInfo'])
		},
		methods: {
			// 获取收藏列表
			async collectList(){
				const response = await this.$api.user.collectList(this.userInfo.id)
				if(response.statusCode===200){
					this.strategy = response.data
					console.log(response.data)
				}
			},
			// 跳转到攻略详情页
			toStrategyDetail(strategyid){
				const url = `/pages/strategy/details?strategyid=${strategyid}`
				uni.navigateTo({
					url:url
				})
			}
		},
		onLoad() {
			this.collectList()
		}
	}
</script>

<style scoped lang="scss">
	// 攻略列表样式
	.strategy-item{
		margin: 10upx;
		background-color: #fff;
		height: 300upx;
		box-shadow: 0 0 5px #9d9d9d;
		border-radius: 10upx;
		display: flex;
		.left_img{
			height: 300upx;
			width: 400upx;
			.recommend_img{
				height: 300upx;
				width: 400upx;
				font-size: 50upx;
				font-weight: bolder;
				text-align: center;
				line-height: 300upx;
				color: grey;
			}
		}
		.middle_other{
			text-align: center;
			margin-top: 30upx;
			.name{
				font-weight: bolder;
				font-size: 40upx;
			}
			.desc{
				height: 170upx;
				padding: 15upx 15upx;
			}
		}
	}
</style>