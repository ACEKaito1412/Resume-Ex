from flask_limiter import Limiter
from flask import request, jsonify

def get_token_from_header():
    auth = request.headers.get("Authorization", "")

    if auth.startswith("Bearer "):
        return auth.split(" ", 1)[1]
    
    return request.remote_addr

limiter = Limiter(
    key_func=get_token_from_header,
    default_limits=["5 per minute"],
    on_breach=lambda: (
        jsonify({"error": "Rate limit exceeded. Please wait."}),
        429,
    ),
    )