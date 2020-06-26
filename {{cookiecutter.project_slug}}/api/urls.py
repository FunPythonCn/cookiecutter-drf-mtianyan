from api import views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter

from api.views import BaseCountView, LoginView, UploadView, ProductSaveView, ProductSearchView, ProductDetailView

router = DefaultRouter(trailing_slash=False)

router.register('mmall_cart/?', views.MmallCartViewSet)

router.register('category/get_category.do?', views.MmallCategoryViewSet)

router.register('mmall_order/?', views.MmallOrderViewSet)

router.register('mmall_order_item/?', views.MmallOrderItemViewSet)

router.register('mmall_pay_info/?', views.MmallPayInfoViewSet)

router.register('product/list.do/?', views.MmallProductViewSet)

router.register('mmall_shipping/?', views.MmallShippingViewSet)

router.register('user/list.do?', views.MmallUserViewSet)

urlpatterns = [
    re_path('^', include(router.urls)),
    path('statistic/base_count.do', BaseCountView.as_view()),
    path('user/login.do', LoginView.as_view()),
    path('product/upload.do', UploadView.as_view()),
    path('product/save.do', ProductSaveView.as_view()),
    path('product/search.do', ProductSearchView.as_view()),
    path('product/detail.do', ProductDetailView.as_view())
]
