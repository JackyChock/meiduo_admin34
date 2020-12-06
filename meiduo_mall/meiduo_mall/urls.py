"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('verifycations.urls')),
    path('', include('contents.urls')),
    path('', include('oauth.urls')),
    path('', include('areas.urls')),
    path('', include('goods.urls')),
    # url(r'^search/', include('haystack.urls')),
    path('', include('carts.urls')),
    path('', include('orders.urls')),
    path('', include('payments.urls')),
    path('meiduo_admin/', include('meiduo_admin.urls')),

]