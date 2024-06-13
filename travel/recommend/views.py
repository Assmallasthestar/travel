# 推荐前台接口
#
# 1.推荐首页：
#     返回搜索框结果
#     返回推荐列表（分页)
#
# 2.评分推荐
# 3.分类获取推荐列表
from django.db.models import Avg
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from recommend.models import Recommend, Grade
from recommend.permission import RecommendPermission
from recommend.serializers import RecommendSerializer, GradeSerializer
from wx.permission import UserPermission


# Create your views here.
# 推荐首页数据获取接口
class IndexView(APIView):

    def get(self, request):
        # 获取推荐列表
        recommends = Recommend.objects.all()
        # 序列化如果有图片字段，返回数据需要补全完整的图片获取域名，需要在序列化时传入请求对象。
        recommends_ser = RecommendSerializer(recommends, many=True, context={'request': request})
        result = dict(
            recommends=recommends_ser.data
        )
        return Response(result)


# 推荐视图集
class RecommendView(ReadOnlyModelViewSet):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer
    # 实现通过推荐分类进行过滤
    filterset_fields = ('sort', )
    # 实现通过评分和创建时间排序
    ordering_fields = ('rate', 'create_time')


# 搜索推荐视图集
class SearchRecommendView(ReadOnlyModelViewSet):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer
    # 实现通过推荐名称进行过滤
    filterset_fields = ('name', )


# 评分视图集
class GradeView(GenericViewSet, mixins.ListModelMixin):

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    # 实现通过推荐进行过滤
    filterset_fields = ('recommend', 'user')
    # recommend = Recommend.objects
    # 设置认证用户才能访问
    permission_classes = [IsAuthenticated, RecommendPermission]

    def update_grade(self, request, *args, **kwargs):
        # 更新评分
        rate = request.data.get('grade')
        rid = request.data.get('recommend')
        recommend_rate = Recommend.objects.filter(id=rid)
        # 校验参数
        if not rate:
            return Response({'error': "评分不能为空"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        # 修改评分
        Grade.objects.update_or_create(
            recommend=recommend_rate.first(), user=request.user,
            defaults={"rate": rate})
        # 修改recommend评分
        avg = Grade.objects.filter(recommend__id=rid).aggregate(ave=Avg("rate"))
        ave = round(avg['ave'])
        recommend_rate.update(rate=ave)
        return Response({'message': "评分成功"}, status=status.HTTP_200_OK)
