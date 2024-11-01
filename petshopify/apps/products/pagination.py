from rest_framework.pagination import PageNumberPagination


class DynamicPageNumberPagination(PageNumberPagination):
    page_size_query_param = "page_size"  # Allow the client to set page size
    max_page_size = (
        100  # Optional: Set a maximum limit for page size to prevent large data loads
    )

