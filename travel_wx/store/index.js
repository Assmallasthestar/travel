// 页面路径：store/index.js 
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);//vue的插件机制

//Vuex.Store 构造器选项
const store = new Vuex.Store({
	// 全局数据
	state:{
		token: "",
		refresh: "",
		userInfo: {},
		// 用户是否登录
		isAuth: false,
		// 当前位置
		pos: ""
	},
	// 全局的计算属性
	getters:{
		
	},
	// 修改数据的方法
	mutations:{
		// 保存登录后的用户信息
		saveLoginStatus(state, info){
			// console.log('vuex:',info)
			state.isAuth = true
			state.token = info.token
			// 存储到uniapp提供的持久化数据存储仓库
			uni.setStorage({
				key: "isAuth",
				data: true
			})
			uni.setStorageSync("token",info.token)
			uni.setStorage({
				key: "refresh",
				data: info.refresh
			})
		},
		// 保存用户信息
		saveUserInfo(state,user){
			state.userInfo = user
			uni.setStorage({
				key:"userinfo",
				data:user
			})
		},
		// 退出登录
		logOut(state){
			// 清空vuex中的用户信息
			state.isAuth = false
			state.userInfo = {}
			//清空uni-appStorage中用户信息
			uni.clearStorage()
			// 重定向首页
			uni.switchTab({
				url:"/pages/index/index"
			})
		}
	},
	// 全局操作的方法
	actions:{
		
	}
})
export default store
