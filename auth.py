
# ملف إدارة الأكواد: auth.py

import datetime

codes = {
    "عمكالجعفري": {
        "type": "permanent",
        "activated": True,
        "created_at": "2025-06-15",
    },
    "عباس": {
        "type": "temporary",
        "activated": True,
        "created_at": "2025-06-15",
        "expires_at": "2025-07-15",
    }
}

def is_code_valid(code):
    data = codes.get(code)
    if not data:
        return False
    if data["type"] == "temporary":
        today = datetime.date.today()
        expires = datetime.datetime.strptime(data["expires_at"], "%Y-%m-%d").date()
        return today <= expires and data["activated"]
    return data["activated"]
