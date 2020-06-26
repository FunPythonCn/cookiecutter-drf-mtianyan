from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import MmallCart, MmallCategory, MmallOrder, MmallOrderItem, MmallPayInfo, MmallProduct, MmallShipping, MmallUser
from api.serializers import MmallCartSerializer, MmallCategorySerializer, MmallOrderSerializer, MmallOrderItemSerializer, MmallPayInfoSerializer, \
    MmallProductSerializer, MmallShippingSerializer, MmallUserSerializer
from drf_mmall.pagination import CategoryPagination, CustomPageNumberPagination


class MmallCartViewSet(viewsets.ModelViewSet):
    serializer_class = MmallCartSerializer
    queryset = MmallCart.objects.all()


class MmallCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = MmallCategorySerializer
    pagination_class = CategoryPagination
    queryset = MmallCategory.objects.all()


class MmallOrderViewSet(viewsets.ModelViewSet):
    serializer_class = MmallOrderSerializer
    queryset = MmallOrder.objects.all()


class MmallOrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = MmallOrderItemSerializer
    queryset = MmallOrderItem.objects.all()


class MmallPayInfoViewSet(viewsets.ModelViewSet):
    serializer_class = MmallPayInfoSerializer
    queryset = MmallPayInfo.objects.all()


class MmallProductViewSet(viewsets.ModelViewSet):
    serializer_class = MmallProductSerializer
    queryset = MmallProduct.objects.all()


class MmallShippingViewSet(viewsets.ModelViewSet):
    serializer_class = MmallShippingSerializer
    queryset = MmallShipping.objects.all()


class MmallUserViewSet(viewsets.ModelViewSet):
    serializer_class = MmallUserSerializer
    queryset = MmallUser.objects.all()


class BaseCountView(APIView):
    def get(self, request):
        return Response({"status": 0, "data": {"userCount": 803, "productCount": 1168, "orderCount": 761}})


class LoginView(APIView):
    def post(self, request):
        isAdmin = request.data["isAdmin"]
        username = request.data["username"]
        password = request.data["password"]
        return Response({"status": 0, "data": {"userCount": 803, "productCount": 1168, "orderCount": 761}})


class UploadView(APIView):
    def post(self, request):
        return Response({"status": 0, "data": {"uri": "2935276d-33cf-4f57-a63c-dd54a4fd6623.png",
                                               "url": "http://img.happymmall.com/2935276d-33cf-4f57-a63c-dd54a4fd6623.png"}})


class ProductSaveView(APIView):
    def get(self, request):
        return Response({"status": 0, "data": "新增产品成功"})


class ProductSearchView(APIView):
    """
    listType: search
    pageNum: 1
    productName: 123
    """
    def get(self, request):
        query_result = MmallProduct.objects.all()
        paginator = CustomPageNumberPagination()
        result_page = paginator.paginate_queryset(query_result, request)
        return paginator.get_paginated_response(MmallProductSerializer(result_page, many=True).data)


class ProductDetailView(APIView):
    def get(self, request):
        product_id = request.query_params["productId"]
        print(product_id)
        product = MmallProduct.objects.get(id=product_id)
        return Response({
            "status": 0,
            "data": MmallProductSerializer(product).data
        })