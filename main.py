from flask import Flask
from app.routes.upload_route import upload_bp
from app.routes.analyze_route import analyze_bp, init_analyze_route
from app.services.file_service import save_document
from app.services.resume_extractor import ModelExtractor
import os

base_path = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_path, "app", "models", "Qwen3-0.6B-Q4_K_M.gguf")
service_extractor = ModelExtractor(model_path=model_path)


init_analyze_route(service_extractor)


app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(upload_bp)
app.register_blueprint(analyze_bp)


if __name__ == "__main__":
    app.run(debug=True)