<template>
	<view class="container">
		<!-- 富文本编辑器 -->
		<view>
		    <view class="tools">
				<!-- 标题 -->
		        <view class="item"><text :style="titleShow?'color:#0199fe' :'color:#333333'" @click="addTitle" class="iconfont icon-zitibiaoti"></text></view>
		        <!-- 加粗 -->
				<view class="item"><text :style="titleBold?'color:#0199fe' :'color:#333333'" @click="addBold" class="iconfont icon-zitijiacu"></text></view>
				<!-- 斜体 -->
		        <view class="item"><text :style="titleItalic?'color:#0199fe' :'color:#333333'" @click="addItalic" class="iconfont icon-zitixieti"></text></view>
				<!-- 下划线 -->
		        <view class="item"><text :style="titleUnderline?'color:#0199fe' :'color:#333333'" @click="addUnderline" class="iconfont icon-zitixiahuaxian"></text></view>
				<!-- 分割线 -->
		        <view class="item"><text @click="addDivider" class="iconfont icon-fengexian"></text></view>
				<!-- 图片 -->
		        <view class="item"><text @click="addImage" class="iconfont icon-charutupian"></text></view>
		    </view>
		    <view class="content">
		        <editor 
					show-img-size
					show-img-toolbar
					show-img-resize
					@ready="onEditorReady"
					class="myEditor" 
					placeholder="写点什么儿~"
				></editor>
		    </view>
		    <view class="btn">
		        <button type="primary">确定</button>
		    </view>
		</view>
	</view>

</template>

<script>
	export default {
		data() {
			 return {
				 titleShow:false,
				 titleBold:false,
				 titleItalic:false,
				 titleUnderline:false
			 }
		},
		methods:{
			onEditorReady(){
			    uni.createSelectorQuery().in(this).select('.myEditor').fields({
			        context:true
			    },res=>{
			        console.log(res);
			        this.editorCtx = res.context
			    }).exec()
			},
			// 分割线
			addDivider(){
			    this.editorCtx.insertDivider()
			},
			// 标题
			addTitle(){
			    this.titleShow=!this.titleShow 
			    this.editorCtx.format('header',this.titleShow?'H2':false)
			},
			// 加粗
			addBold(){
				this.titleBold=!this.titleBold
				this.editorCtx.format('bold')
			},
			// 斜体
			addItalic(){
				this.titleItalic=!this.titleItalic
				this.editorCtx.format('italic')
			},
			// 下划线
			addUnderline(){
				this.titleUnderline=!this.titleUnderline
				this.editorCtx.format('underline')
			},
			// 图片
			addImage(){
			    uni.chooseImage({
			        success:res=>{
			            uni.showLoading({
			                title:'loading...'
			            })
			            for(let i=0;i<res.tempFilePaths.length;i++){
			                this.editorCtx.insertImage({
			                    src:res.tempFilePaths[i]
			                })
			            }
			            uni.hideLoading()
			        }
			    })
			}
		}
	}
</script>

<style scoped lang="scss">
	.tools{
		display: flex;
		justify-content: space-around;
		margin-top: 30upx;
		.item{
			font-size: 30upx;
		}
	}
	.content{
		margin: 30upx 15upx;
	}
	.myEditor{
		height: 1000upx;
	}
	.btn{
		border-radius: 40upx;
		background-color: $uni-primary;
		color:white;
		margin: 30upx 15upx;
	}
</style>