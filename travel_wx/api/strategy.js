// 攻略模块封装接口
import http from './request.js'

export default{
	// 获取攻略的数据
	getStrategyData(){
		return http.get('/api/strategy/index/')
	},
	// 获取单个攻略的数据
	getStrategyDetail(strategyId){
		return http.get(`/api/strategy/strategy/${strategyId}/`)
	},
	// 获取攻略评论区列表
	getCommentList(params){
		return http.get('/api/strategy/strategy/comment/',params)
	},
	// 是否收藏攻略
	getIsCollect(params){
		return http.get('/api/strategy/isCollect/',params,true)
	},
	// 是否点赞攻略
	getIsLike(params){
		return http.get('/api/strategy/isLike/',params,true)
	},
	// 收藏攻略
	collectStrategy(params){
		return http.post('/api/strategy/collect/',params,true)
	},
	// 点赞攻略
	likeStrategy(params){
		return http.post('/api/strategy/like/',params,true)
	},
	// 取消收藏
	deleteCollect(id){
		return http.delete(`/api/strategy/collect/${id}/`,true)
	},
	// 取消点赞
	deleteLike(id){
		return http.delete(`/api/strategy/like/${id}/`,true)
	},
	// 评论攻略
	commentStrategy(params){
		return http.post('/api/strategy/comment/',params,true)
	},
	deleteComment(id){
		return http.delete(`/api/strategy/comment/${id}/`,true)
	}
}