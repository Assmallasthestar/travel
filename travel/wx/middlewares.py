from django.utils.deprecation import MiddlewareMixin

# 自定义中间类


class MiddlewareHead(MiddlewareMixin):

    @staticmethod
    # 在视图函数之后执行的。
    def process_response(request, response):
        if request:
            response['Access-Control-Allow-Origin'] = '*'
        return response
