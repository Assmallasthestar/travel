<template>
	<view class="container">
		<view class="search">
			<view class="searchcol">
				<input class="searchbox" type="text" placeholder="请输入" focus="true" v-model="inputValue">
			</view>
			<view class="searchtext" @click="getSearch">搜索</view>
		</view>
		<!-- 推荐列表 -->
		<view class="recommend-item" v-if="isShow">
			<view class="left_img">
				<image v-if="recommend.img" class="recommend_img" :src="recommend.img" mode="aspectFill"></image>
				<view v-else class="recommend_img">暂无图片</view>
			</view>
			<view class="middle_other">
				<view class="name">{{recommend.name}}</view>
				<view class="desc" v-if="recommend.desc">{{recommend.desc}}</view>
				<view class="desc" v-else>
				</view>
				<view class="rate">
					<uni-rate :readonly="true" :value="recommend.rate" color="#B0C4DE" active-color="#87CEEB" />
				</view>
			</view>
			<!-- 评分按钮 -->
			<view class="right_mark"  @click="open(recommend.id)">
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
				recommendid:'',
				rate:'',
				gradeFormData:{
					grade:'',
					recommend:''
				},
				recommend: [],
				inputValue: "",
				searchFormData:{
					name:''
				},
				isShow:'false'
			}
		},
		computed:{
			...mapState(['userInfo']),
		},
		methods: {
			// 打开弹窗
			open(id){
				// 通过组件定义的ref调用uni-popup方法 ,如果传入参数 ，type 属性将失效 ，仅支持 ['top','left','bottom','right','center']
				this.$refs.popup.open('center')
				this.getSortData(id)
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
					this.getSearch()
				}
			},
			// 搜索结果
			async getSearch(){
				this.searchFormData.name = this.inputValue
				const response = await this.$api.recommend.getSearch(this.searchFormData)
				if(response.statusCode===200){
					this.recommend = response.data.results[0]
					if(this.recommend){
						this.isShow = true
					}else{
						this.isShow = false
					}
				}
			}
		},
		onLoad() {
			this.isShow=false
		}
	}
</script>

<style scoped lang="scss">
	.container{
		
	}
	// 搜索栏样式
	.search{
		display: flex;
		margin-top: 30upx;
		margin-bottom: 20upx;
		height: 80upx;
		.searchcol {
			width: 80%;
			border: 2upx solid $uni-primary;
			border-radius: 30upx;
			margin-left: 3%;
			display: flex;
			// padding-left: 50%;
			.searchbox{
				font-size: 40upx;
				height: 70upx;
				padding-left: 30upx;
			}
		}
		.searchtext{
			color: $uni-primary;
			font-size: 40upx;
			margin-left: 25upx;
			line-height: 80upx;
		}
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