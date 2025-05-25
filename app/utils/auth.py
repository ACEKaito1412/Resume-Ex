from functools import wraps
from flask import request, jsonify


# testing
VALID_TOKENS = ['insecure_auth_token_1', 'insecure_auth_token_2']

def is_authorized(token:str)->bool:
    print(token)
    print(VALID_TOKENS[0])
    return token in VALID_TOKENS


def require_token(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        token = auth_header.replace("Bearer", "").strip()
        
        print(token)
        if  not is_authorized(token):
            return jsonify({"error" : "Unauthorized"}), 401
        
        return f(*args, **kwargs)
    
    return decorated