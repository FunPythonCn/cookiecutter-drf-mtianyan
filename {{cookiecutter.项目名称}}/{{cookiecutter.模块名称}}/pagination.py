from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPageNumberPagination(PageNumberPagination):
    page_query_param = 'current'
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):
        return Response({
            "status": 0,
            "data": OrderedDict([
                ('total', self.page.paginator.count),
                ('list', data),
                ('pageNum', self.page.paginator.num_pages),
                ('pageSize', self.page.paginator.per_page)
            ])
        })


class CategoryPagination(PageNumberPagination):
    page_query_param = 'current'
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):
        return Response({
            "status": 0,
            "data": data})