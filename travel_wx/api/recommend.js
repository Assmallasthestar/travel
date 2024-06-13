// 推荐模块封装接口
import http from './request.js'

export default{
	// 获取推荐的数据
	getRecommendData(){
		return http.get('/api/recommend/index/')
	},
	getSearch(params){
		return http.get('/api/recommend/search/',params)
	},
	// 获取推荐分类数据
	getRecommendSortData(params){
		return http.get('/api/recommend/recommend/',params)
	},
	// 获取用户当前推荐评分
	getUserRecommendSort(id,params){
		return http.get(`/api/recommend/${id}/rate/`,params,true)
	},
	// 用户评分
	updateUserRate(id,params){
		return http.put(`/api/recommend/${id}/rate/`,params,true)
	}
}