from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views.statistical import UserTotalCountView

urlpatterns = [
    path('authorizations/', obtain_jwt_token),
    # ------------  数据统计  ------------
    path('statistical/total_count/', UserTotalCountView.as_view()),

]
