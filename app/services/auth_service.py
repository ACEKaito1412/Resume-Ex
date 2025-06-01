from extensions.db import db
from app.model.user_model import User
from werkzeug.security import generate_password_hash
import secrets

def create_user(username:str, password:str)->str:

    token = "rex-" + secrets.token_hex(30)

    new_user = User(
        user_name = username,
        password = generate_password_hash(password=password),
        token = token
    )

    db.session.add(new_user)
    db.session.commit()
    
    return token