import pickle
from coursework import settings
from users.models import CustomUser, Visit
from django.core.cache import cache
import json
import redis


class VisitDataBaseService:
    def save_to_db(self):
        redis_client = redis.StrictRedis(host="redis", port=settings.REDIS_PORT)

        keys = redis_client.keys(
            f"{settings.CACHES['default']['KEY_PREFIX']}:1:visit:*"
        )

        for key in keys:
            data_raw = redis_client.get(key)
            if data_raw:
                data = pickle.loads(data_raw)
                data = json.loads(data)

                user_id = data["user"]
                user = None
                if user_id != "anonymous":
                    user = CustomUser.objects.get(id=user_id)

                visit = Visit(
                    user=user,
                    visit_date=data["visit_date"],
                    request_info=data["request_info"],
                )
                visit.save()

                redis_client.delete(key)
