from datetime import date
import uuid


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {"is_new": False}

    fields = {
        "email": details.get("email"),
        "firstname": details.get("given_name", ""),
        "lastname": details.get("family_name", ""),
        "registration_date": date.today(),
        "password": str(uuid.uuid4()),
    }
    return {"is_new": True, "user": strategy.create_user(**fields)}
