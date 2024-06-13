<template>
	<view class="container">
		<!-- 手机状态栏 -->
		<view class="status_bar"></view>
		<!-- 地区分类 -->
		<view class="topbar">
			<view class="pos">
				<!-- 省市区选择器 -->
				<uni-data-picker :localdata="items" popup-title="请选择地区" @change="onchange" @nodeclick="onnodeclick">
				</uni-data-picker>
			</view>
		</view>
		<!-- 搜索栏 -->
		<view class="search">
			<input class="searchbox" type="text" placeholder="请输入" @focus="toSearch">
		</view>
		<!-- 推荐分类 -->
		<view class="top_box">
			<navigator class="classify" url="food">
				<image class="icon" src="@/static/recommend/food.png" mode="aspectFit"></image><br>
				<text class="text">美食</text>
			</navigator>
			<navigator class="classify" url="spot">
				<image class="icon" src="@/static/recommend/spot.png" mode="aspectFit"></image><br>
				<text class="text">景点</text>
			</navigator>
			<navigator class="classify" url="hotel">
				<image class="icon" src="@/static/recommend/hotel.png" mode="aspectFit"></image><br>
				<text class="text">住宿</text>
			</navigator>
		</view>
		<!-- 热门推荐图标 -->
		<view class="fire">
			<uni-icons color="#ff557f" type="fire-filled" size="30"></uni-icons>
			<text>热门推荐</text>
		</view>
		<!-- 推荐列表 -->
		<view class="recommend-item" v-for='r in recommend' :key='r.id'>
			<view class="left_img">
				<image v-if="r.img" class="recommend_img" :src="r.img" mode="aspectFill"></image>
				<view v-else class="recommend_img">暂无图片</view>
			</view>
			<view class="middle_other">
				<view class="name">{{r.name}}</view>
				<view class="desc" v-if="r.desc">{{r.desc}}</view>
				<view class="desc" v-else>
				</view>
				<view class="rate">
					<uni-rate :readonly="true" :value="r.rate" color="#B0C4DE" active-color="#87CEEB" />
				</view>
			</view>
			<!-- 评分按钮 -->
			<view class="right_mark"  @click="open(r.id)">
				<view class="mark">
					<image class="mark_img" src="@/static/recommend/mark.png"></image>
				</view>
			</view>
		</view>
		<!-- 评分弹窗 -->
		<uni-popup ref="popup" background-color="#fff" :mask-click="false">
			<view class="popup-content" >
				<view class="ratetext">推荐指数</view>
				<view class="rate">
					<uni-rate v-model="rate" @change="onChange" size="30" :max="5" color="#B0C4DE" active-color="#87CEEB"/>
				</view>
				<button @click="close">确认</button>
			</view>
		</uni-popup>
		<!-- 底层tarbar -->
		<view class="bottom-tarbar"></view>
	</view>
</template>

<script>
	// import address from '@/static/address.js'

	import { mapState} from 'vuex'
	export default {
		data() {
			return {
				recommendid:'',
				rate:'',
				formData:{
					recommend:'',
					user:''
				},
				gradeFormData:{
					grade:'',
					recommend:''
				},
				recommend: [],
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
		computed:{
			...mapState(['userInfo']),
		},
		methods: {
			// 获取首页数据
			async getData() {
				const response = await this.$api.recommend.getRecommendData()
				// console.log('数据结果',response)
				if(response.statusCode===200){
					this.recommend = response.data.recommends
				}
			},
			// 打开弹窗
			open(id){
				// 通过组件定义的ref调用uni-popup方法 ,如果传入参数 ，type 属性将失效 ，仅支持 ['top','left','bottom','right','center']
				this.$refs.popup.open('center')
				this.getSortData(id)
			},
			// 获取用户推荐分类数据
			async getSortData(id){
				this.formData.recommend=id
				this.recommendid=id
				this.formData.user=this.userInfo.id
				const response = await this.$api.recommend.getUserRecommendSort(this.userInfo.id,this.formData)
				if(response.statusCode===200){
					if(response.data.count!==0){
						this.rate = response.data.results[0].rate
					}else{
						this.rate = 0
					}
				}
			},
			// 弹窗关闭
			close() {
				this.putGradeData()
				this.$refs.popup.close()
			},
			// 评分改变
			onChange(e){
				this.value = e.value
			},
			// 用户评分
			async putGradeData(){
				this.gradeFormData.grade=this.rate
				this.gradeFormData.recommend=this.recommendid
				const response = await this.$api.recommend.updateUserRate(this.userInfo.id,this.gradeFormData)
				if(response.statusCode===200){
					uni.showToast({
						title:"评分成功！"
					})
					// 更新首页数据
					this.getData()
				}
			},
			// 跳转搜素界面
			toSearch(){
				uni.navigateTo({
					url:'/pages/index/search'
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
	// 推荐分类样式
	.top_box {
		height: 300upx;
		// background: $uni-primary;
		background-color: #E3F2FD;	
		text-align: center;
		display: flex;
		justify-content: space-around;
		.classify{
			width: 200upx;
			height: 200upx;
			border-radius: 100upx;
			margin-top: 60upx;
			margin-left: 10upx;
			margin-right: 10upx;
			margin-bottom: 40upx;
			background-color: white;
			// flex-direction: row;
			.icon{
				height: 150upx;
				width: 150upx;
				
			}
			.text{
				font-size: 30upx;
			}
		}
	}
	// 热门推荐图标样式
	.fire{
		font-size: 30upx;
		color: #ff557f;
		height: 80upx;
		line-height: 80upx;
	}
	// 推荐列表样式
	.recommend-item{
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
				line-height: 40upx;
				width: 200upx;
				overflow: hidden;
				text-overflow: ellipsis;
				white-space: nowrap;
			}
			.desc{
				height: 170upx;
				padding: 5upx 15upx;
			}
		}
		.mark_img{
			height: 80upx;
			width: 80upx;
			line-height: 100upx;
			border: 1px solid grey;
			box-shadow: 0 0 5px #9d9d9d;
			border-radius: 30%;
			margin-top: 110upx;
		}
	}
	.popup-content{
		height: 300upx;
		width: 600upx;
		.ratetext{
			font-size: 30upx;
			color: $uni-primary;
			text-align: center;
			padding: 50upx 0;
			padding-bottom: 30upx;
		}
		.rate{
			margin: 0 150upx;
			margin-bottom: 30upx;
		}
		button{
			margin: 0 30upx;
			color: #fff;
			background-color: $uni-primary;
		}
	}
	.bottom-tarbar{
		padding-bottom: var(--window-bottom);
	}
</style>
