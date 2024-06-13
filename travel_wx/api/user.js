// 用户模块接口封装
import http from './request.js'

export default{
	// 微信登录接口
	wxLogin(params){
		return http.post('/api/users/wx_login/',params)
	},
	// 登录接口
	login(params) {
		return http.post('/api/users/login/', params)
	},
	// 获取用户信息
	getUserInfo(id){
		return http.get(`/api/users/users/${id}/`,{},true)
	},
	// 刷新token
	
	// 校验token
	
	// 修改头像
	updateImg(id,params){
		return http.post(`/api/users/${id}/avatar/upload`, params, true)
	},
	// 修改昵称
	updateNickName(id,params){
		return http.put(`/api/users/${id}/name/`, params, true)
	},
	//修改性别
	updateGender(id,params){
		return http.put(`/api/users/${id}/gender/`, params, true)
	},
	//修改邮箱
	updateEmail(id,params){
		return http.put(`/api/users/${id}/email/`, params, true)
	},
	//修改密码
	updatePassword(id,params){
		return http.put(`/api/users/${id}/password/`, params, true)
	},
	// 问题反馈
	createFeedback(params){
		return http.put(`/api/users/feedback/`, params, true)
	},
	// 我的收藏列表
	collectList(id){
		return http.get(`/api/strategy/myCollect/${id}/`,{},true)
	}
}