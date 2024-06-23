from datetime import datetime
import json
from django.core.cache import cache


class VisitCacheService:
    def __init__(self, request, response):
        self.request = request
        self.response = response

    def add_to_cache(self) -> bool:
        data = self._prepare_visit_data()
        key = self._get_key_name()
        return cache.set(key, json.dumps(data))

    def _prepare_visit_data(self):
        user_id = (
            self.request.user.id if self.request.user.is_authenticated else "anonymous"
        )
        data = {
            "user": user_id,
            "visit_date": datetime.now().isoformat(),
            "request_info": f"{self.request.GET} {self.request.POST} {self.request.headers.get('User-Agent')}",
        }
        return data

    def _get_key_name(self):
        return f"visit:{self.request.path}:{datetime.now().timestamp()}"
