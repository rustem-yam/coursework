from django.utils.deprecation import MiddlewareMixin
from users.services.visit_cache_service import VisitCacheService


class VisitMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.path.startswith("/admin/"):
            service = VisitCacheService(request, response)
            service.add_to_cache()
        return response
