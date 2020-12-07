from rest_framework.generics import ListAPIView
from meiduo_admin.serialziers.user import UserSerializer
from meiduo_admin.utils import UserPageNum
from users.models import User


class UserView(ListAPIView):
    # 指定使用的序列化器
    serializer_class = UserSerializer
    # 指定分页器
    pagination_class = UserPageNum

    # 重写get_queryset方法，根据前端是否传递keyword值返回不同查询结果
    def get_queryset(self):
        # 获取前端传递的keyword值
        keyword = self.request.query_params.get('keyword')
        # 如果keyword是空字符，则说明要获取所有用户数据
        if keyword is '' or keyword is None:
            return User.objects.all()
        else:
            return User.objects.filter(username=keyword)