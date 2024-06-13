<template>
	<view class="detail-box">
		<!-- 底部导航栏 -->
		<view class="bottom-tarbar">
			<!-- 评论 -->
			<view class="comment">
				<uni-easyinput v-model="commentValue" placeholder="点我发评论" @focus="open" maxlength="999"></uni-easyinput>
			</view>
			<!-- 右侧图标 -->
			<view class="right-icon">
				<view class="icon">
					<uni-icons type="star-filled" size="30" v-if="isCollect" color="#00BFFF" @click="deleteCollect"></uni-icons>
					<uni-icons type="star" size="30" v-else @click="collectStrategy"></uni-icons>
				</view>
				<view class="icon">
					<uni-icons type="chatbubble" size="30" @click="toComment"></uni-icons>
				</view>
				<view class="icon">
					<uni-icons type="hand-up-filled" size="30" v-if="isLike" color="#00BFFF" @click="deleteLike"></uni-icons>
					<uni-icons type="hand-up" size="30" v-else @click="likeStrategy"></uni-icons>
				</view>
			</view>
		</view>
		<!-- 评论弹窗 -->
		<uni-popup ref="popup" background-color="#fff">
			<view class="popup-content" >
				<uni-easyinput v-model="commentValue" placeholder="点我发评论" focus="true" type="textarea" maxlength="999" autoHeight></uni-easyinput>
				<button @click="close">发布</button>
			</view>
			<!-- 底部tabrar -->
			<view class="tarbarheight"></view>
		</uni-popup>
		<!-- 攻略标题 -->
		<text class="strategy-title">{{strategy.title}}</text>
		<!-- 攻略描述 -->
		<text class="strategy-desc" v-if="strategy.desc">{{strategy.desc}}</text>
		<!-- 内容 -->
		<view class="detail-info">
			<rich-text :nodes="strategy.content"></rich-text>
		</view>
		<!-- 评论区 -->
		<view class="comment-area" v-for="c in commentList" :key="c.id" v-if="boolean">
			<hr>
			<view class="userInfo">
				<image :src="userInfo.avatar" class="user-icon" mode="aspectFit"></image>
				<view class="user-info">{{userInfo.nick_name}}</view>
				<uni-icons class="delete" v-if="userInfo.id===c.user" type="trash" size="30" @click="deleteComment(c.id)" color="red"></uni-icons>
			</view>
			<view class="comment-content">{{c.content}}</view>
		</view>
		<!-- 底部tabrar -->
		<view class="tarbarheight"></view>
	</view>
</template>

<script>
	import { mapState } from 'vuex'
	
	export default{
		data(){
			return{
				// 当前攻略id
				strategyid: '',
				// 攻略数据
				strategy: {},
				// 用户攻略id数据
				strategyUserData: {
					user: '',
					strategy: ''
				},
				// 是否收藏
				isCollect: '',
				// 是否点赞
				isLike: '',
				// 收藏id
				collectId: '',
				// 点赞id
				likeId: '',
				// 评论数据
				commentData:{
					user: '',
					strategy: '',
					content: ''
				},
				// 评论内容
				commentValue: '',
				// 加载评论区数据参数
				commentArea:{
					strategy:''
				},
				// 评论区列表
				commentList: [],
				// 刷新评论区v-for
				boolean: 'true'
			}
		},
		methods:{
			// 发送请求到后台，加载攻略数据
			async getStrategyDetail(){
				const response = await this.$api.strategy.getStrategyDetail(this.strategyid)
				if(response.statusCode===200){
					this.strategy = response.data
				}
			},
			// 加载评论区列表
			async getCommentList(){
				const response = await this.$api.strategy.getCommentList(this.commentArea)
				if(response.statusCode===200){
					this.commentList = response.data.results
					for(let i=0; i<response.data.count;i++){
						const response = await this.$api.strategy.getAvatarName(this.commentList.id)
					}
				}
			},
			// 查询攻略是否已收藏
			async getIsCollect(){
				const response = await this.$api.strategy.getIsCollect(this.strategyUserData)
				if(response.statusCode===200){
					this.isCollect = true
					this.collectId = response.data.collect[0].id
				}
			},
			// 查询攻略是否已点赞
			async getIsLike(){
				const response = await this.$api.strategy.getIsLike(this.strategyUserData)
				if(response.statusCode===200){
					this.isLike = true
					this.likeId = response.data.like[0].id
				}
			},
			// 收藏攻略
			async collectStrategy(){
				const response = await this.$api.strategy.collectStrategy(this.strategyUserData)
				if(response.statusCode===201){
					this.isCollect = true
				}
			},
			// 点赞攻略
			async likeStrategy(){
				const response = await this.$api.strategy.likeStrategy(this.strategyUserData)
				if(response.statusCode===201){
					this.isLike = true
				}
			},
			// 取消收藏
			async deleteCollect(){
				this.getIsCollect()
				const response = await this.$api.strategy.deleteCollect(this.collectId)
				if(response.statusCode===204){
					this.isCollect = false
				}
			},
			// 取消点赞
			async deleteLike(){
				this.getIsLike()
				const response = await this.$api.strategy.deleteLike(this.likeId)
				if(response.statusCode===204){
					this.isLike = false
				}
			},
			// 打开评论弹窗
			open(){
				// 通过组件定义的ref调用uni-popup方法 ,如果传入参数 ，type 属性将失效 ，仅支持 ['top','left','bottom','right','center']
				this.$refs.popup.open('bottom')
			},
			// 评论攻略
			async commentStrategy(){
				this.commentData.user = this.strategyUserData.user
				this.commentData.strategy = this.strategyUserData.strategy
				this.commentData.content = this.commentValue
				const response = await this.$api.strategy.commentStrategy(this.commentData)
				if(response.statusCode===201){
					uni.showToast({
						title: '评论成功',
						duration: 1000
					})
					this.commentValue = ''
					this.commentList()
				}
			},
			// 评论攻略，弹窗关闭
			close() {
				this.commentStrategy()
				this.$refs.popup.close()
			},
			// 滚动到评论区
			toComment(){
				uni.createSelectorQuery().select('.comment-area').boundingClientRect(data=>{//目标位置的节点：类class或者id
					uni.pageScrollTo({
						duration: 100,//过渡时间
						scrollTop:data.top+590,//到达距离顶部的top值
					})
				}).exec()
			},
			// 删除评论
			async deleteComment(commentId){
				const response = await this.$api.strategy.deleteComment(commentId)
				if(response.statusCode===204){
					this.commentList()
				}
			}
		},
		onLoad(option) {
			this.strategyid = option.strategyid
			this.commentArea.strategy = option.strategyid
			this.strategyUserData.strategy = this.strategyid
			this.strategyUserData.user = this.userInfo.id
			this.getStrategyDetail()
			this.getCommentList()
			this.getIsCollect()
			this.getIsLike()
		},
		computed: {
			...mapState(['userInfo'])
		},
	}
</script>

<style scoped lang="scss">
	.detail-box{
		margin: 10upx 0upx;
	}
	.bottom-tarbar{
		height: 100upx;
		background-color: white;
		width: 100%;
		position: fixed;
		bottom: calc( var(--window-bottom));
		z-index: 1030;
		display: flex;
		.comment{
			width: 45%;
			margin-left: 30upx;
		}
		.right-icon{
			display: flex;
			margin: 30upx 15upx;
			.icon{
				margin: 0 30upx;
				flex: 2 1 auto;
			}
		}
	}
	.popup-content{
		margin: 10upx 30upx;
		button{
			margin-top: 20upx;
			background-color: $uni-primary;
			color: white;
		}
	}
	.strategy-title{
		font-size: 60upx;
		font-weight: bolder;
		width: 100%;
	}
	.strategy-desc{
		font-size: 30upx;
		color: grey;
		width: 100%;
	}
	.detail-info{
		margin-bottom: 30upx;
	}
	.comment-area{
		margin: 30upx 30upx;
		.userInfo{
			display: flex;
			margin: 30upx 0;
			.user-icon{
				width: 60upx;
				height: 60upx;
				background-color: #F0F8FF;
				margin: 0 30upx;
			}
			.user-info{
				color: black;
				font-size: 35upx;
				line-height: 60upx;
				text-align: center;
				height: 60upx;
			}
			.delete{
				 margin-left: auto;
			}
		}
		.comment-content{
			margin: 30upx 0;
			margin-left: 120upx;
			font-size: 30upx;
			line-height: 30upx;
		}
	}
	.tarbarheight{
		height: 105upx;
	}
</style>