from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class PaginationSize20(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size:
            try:
                page_size = int(page_size)
            except ValueError:
                page_size = self.page_size
        else:
            page_size = self.page_size  # Use default if not provided

        return page_size

    def get_paginated_response(self, data):
        limit = self.get_page_size(self.request)
        return {
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "count": self.page.paginator.count,
            "limit": limit,
            "current_page": self.page.number,
            "total_pages": self.page.paginator.num_pages,
            "results": data,
        }
