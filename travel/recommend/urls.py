from django.urls import path, re_path
from .views import *

urlpatterns = [
    # 推荐首页数据获取
    path('index/', IndexView.as_view()),
    # 分类推荐列表接口
    path('recommend/', RecommendView.as_view({"get": "list"})),
    # 搜索推荐接口
    path('search/', SearchRecommendView.as_view({"get": "list"})),
    # 获取评分和评分
    path('<int:pk>/rate/', GradeView.as_view({'get': 'list', "put": "update_grade"})),
]
