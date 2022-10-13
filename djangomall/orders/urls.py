from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 增加视图函数，参数限定为 UUID 类型
    path('<uuid:order_id>/', views.update_order, name='update'),
]