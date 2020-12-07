from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views.statistical import UserTotalCountView, UserDayCountView, UserActiveCountView, UserOrderCountView, \
    UserMonthCountView, GoodsDayView
from .views.users import UserView

urlpatterns = [
    path('authorizations/', obtain_jwt_token),
    # ------------  数据统计  ------------
    path('statistical/total_count/', UserTotalCountView.as_view()),
    path('statistical/day_increment/', UserDayCountView.as_view()),
    path('statistical/day_active/', UserActiveCountView.as_view()),
    path('statistical/day_orders/', UserOrderCountView.as_view()),
    path('statistical/month_increment/', UserMonthCountView.as_view()),
    path('statistical/goods_day_views/', GoodsDayView.as_view()),
    # ------------  用户管理  ------------
    path('users/', UserView.as_view()),

]
