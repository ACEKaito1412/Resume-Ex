from flask import Blueprint, request, jsonify
from app.services.auth_service import create_user

register_bp = Blueprint('register', __name__)

@register_bp.route("/register", methods=["GET", "POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({ "error" : "Missing username and password"})
    
    return jsonify({ "message" : "User created" , "Token" :  create_user(username, password)})