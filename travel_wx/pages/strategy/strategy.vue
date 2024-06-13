<template>
	<view class="container">
		<view class="status_bar">
			<!-- 手机状态栏 -->
		</view>
		<view class="topbar">
			<view class="pos">
				<!-- 省市区选择器 -->
				<uni-data-picker :localdata="items" popup-title="请选择地区" @change="onchange" @nodeclick="onnodeclick">
				</uni-data-picker>
			</view>
		</view>
		<!-- 搜索栏 -->
		<view class="search">
			<input class="searchbox" type="text" placeholder="请输入" focus="true">
		</view>
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
		<uni-fab :pattern="pattern" horizontal="left" vertical="bottom" @fabClick="fabClick" />
	</view>
</template>

<script>
	import { mapState } from 'vuex'
	export default {
		data() {
			return {
				pattern: {
					buttonColor: '#4169E1'
				},
				strategy: [],
				items: [
					{
					  text: "湖南省",
					  value: "1-0",
					  children: [
						{
						  text: "长沙市",
						  value: "1-1"
						},
						{
						  text: "湘西土家族苗族自治州",
						  value: "1-2"
						}
					  ]
					},
					{
					  text: "江西省",
					  value: "2-0",
					  children: [
						{
						  text: "萍乡市",
						  value: "2-1"
						}
					  ]
					},
					{
					  text: "广西壮族自治区",
					  value: "3-0",
					  children: [
							{
							  text: "桂林市",
							  value: "3-1"
							}
					  ]
					},
					{
					  text: "贵州省",
					  value: "4-0",
					  children: [
							{
							  text: "贵阳市",
							  value: "4-1"
							}
					  ]
					},
					{
					  text: "广东省",
					  value: "5-0",
					  children: [
							{
							  text: "深圳市",
							  value: "5-1"
							},
							{
							  text: "肇庆市",
							  value: "5-2"
							},
							{
							  text: "广州市",
							  value: "5-3"
							}
					  ]
					},
				]
			}
		},
		computed: {
			...mapState(['isAuth','userInfo'])
		},
		methods: {
			// 获取攻略数据
			async getData() {
				const response = await this.$api.strategy.getStrategyData()
				if(response.statusCode===200){
					this.strategy = response.data.strategy
				}
			},
			// 进行认证跳转
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
			},
			fabClick(){
				this.navTo('/pages/strategy/create_strategy')
			},
			// 跳转到攻略详情页
			toStrategyDetail(strategyid){
				const url = `/pages/strategy/details?strategyid=${strategyid}`
				uni.navigateTo({
					url:url
				})
			}
		},
		// 加载页面执行的生命周期钩子函数
		onLoad() {
			this.getData()
		}
	}
</script>

<style lang="scss">
	.container {
		font-size: 14upx;
		line-height: 24upx;
	}
	// 手机状态栏样式
	.status_bar{
		height: var(--status-bar-height);
		background-color: $uni-primary;
		width: 100%;
	}
	// 地区分类样式
	.topbar {
		background-color: $uni-primary;
		.pos{
			width: 20%;
			padding: 5upx 5upx;
		}
	}
	// 搜索栏样式
	.search {
		margin-top: 30upx;
		margin-bottom: 20upx;
		width: 80%;
		border: 2upx solid $uni-primary;
		border-radius: 30upx;
		margin-left: 10%;
		// padding-left: 50%;
		.searchbox{
			font-size: 40upx;
			height: 70upx;
			padding-left: 30upx;
		}
	}
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