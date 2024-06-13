"""
URL configuration for travel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.urls import re_path, include

from rest_framework.documentation import include_docs_urls

from wx.views import FileView

API_TITLE = 'API Documents'
API_DESCRIPTION = 'API Information'


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # 用户模块接口
    re_path(r'^api/users/', include('wx.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # 获取图片资源的接口
    re_path(r'file/image/(.+?)/', FileView.as_view()),
    # 推荐模块接口
    re_path(r'^api/recommend/', include('recommend.urls')),
    # 攻略模块接口
    re_path(r'^api/strategy/', include('strategy.urls')),
    # ckeditor富文本路由
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
