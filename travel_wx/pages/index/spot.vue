<template>
	<view class="container">
		<!-- 推荐列表 -->
		<view class="recommend-item" v-for='s in sort' :key='s.id'>
			<view class="left_img">
				<image v-if="s.img" class="recommend_img" :src="s.img" mode="aspectFill"></image>
				<view v-else class="recommend_img">暂无图片</view>
			</view>
			<view class="middle_other">
				<view class="name">{{s.name}}</view>
				<view class="desc" v-if="s.desc">{{s.desc}}</view>
				<view class="desc" v-else>
				</view>
				<view class="rate">
					<uni-rate :readonly="true" :value="s.rate" color="#B0C4DE" active-color="#87CEEB" />
				</view>
			</view>
			<!-- 评分按钮 -->
			<view class="right_mark"  @click="open(s.id)">
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
	</view>
</template>

<script>
	import { mapState} from 'vuex'
	export default {
		data() {
			return {
				Data:{
					sort:'2',
					ordering:'-rate'
				},
				sort:[],
				rate:'',
				formData:{
					recommend:'',
					user:''
				},
				gradeFormData:{
					grade:'',
					recommend:''
				}
			}
		},
		computed:{
			...mapState(['userInfo']),
		},
		methods: {
			// 获取页面数据
			async getData() {
				const response = await this.$api.recommend.getRecommendSortData(this.Data)
				// console.log('数据结果',response)
				if(response.statusCode===200){
					this.sort = response.data.results
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
			}
		},
		// 加载页面执行的生命周期钩子函数
		onLoad() {
			this.getData()
		}
	}
</script>

<style scoped lang="scss">
	.container {
		font-size: 14upx;
		line-height: 24upx;
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
</style>