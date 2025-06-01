from functools import wraps
from flask import request, jsonify
from app import db
from app.model.user_model import User

def is_authorized(token:str)->bool:
    return User.query.filter_by(token=token).first() is not None

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

