from flask import Flask
from extensions.db import db
from app.routes.upload_route import upload_bp, init_upload_route
from app.routes.analyze_route import analyze_bp, init_analyze_route
from app.routes.main_route import main_bp
from app.routes.documentation_route import documentation_bp
from app.routes.register_route import register_bp
from app.services.resume_extractor import ModelExtractor
import os



template_folder = os.path.join(os.path.dirname(__file__), "templates")
print("TEMPLATE FOLDER ABS PATH:", os.path.abspath(template_folder))

def create_app():
    app = Flask(__name__, template_folder=template_folder)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.db"
    db.init_app(app)

    # INIT_SERVICE
    base_path = os.path.abspath(os.path.dirname(__file__))
    model_path = os.path.join(base_path, "lm_model", "Qwen3-0.6B-Q4_K_M.gguf")
    service_extractor = ModelExtractor(model_path=model_path)

    # ROUTE
    init_analyze_route(service_extractor)
    init_upload_route(service_extractor)


    # BLUEPRINT
    app.register_blueprint(main_bp)
    app.register_blueprint(documentation_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(analyze_bp)
    app.register_blueprint(register_bp)

    return app