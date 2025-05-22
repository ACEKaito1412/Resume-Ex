from flask import Flask
from app.routes.upload_route import upload_bp
from app.services.file_service import save_document
from app.services.resume_extractor import ModelExtractor

service_extractor = ModelExtractor('app/models/deepseek-coder-1.3B-kexer-Q4_K_M.gguf')
app = Flask(__name__, template_folder='app/templates')
app.register_blueprint(upload_bp)


if __name__ == "__main__":
    app.run(debug=True)