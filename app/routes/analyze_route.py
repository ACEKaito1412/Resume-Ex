from flask import Blueprint, request, jsonify
from app.services.file_service import process_data
from app.services.resume_extractor import ModelExtractor
from app.utils.auth import require_token
from extensions.limiter import limiter

service_extractor = None

def init_analyze_route(extractor:ModelExtractor):
    global service_extractor
    service_extractor = extractor

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
@require_token
@limiter.limit("5 per minute")
def analyze():
    """
    input_type:  application/json \n
    text: str 
    """
    data = request.get_json()   
    resume_text = data.get("text")

    if not service_extractor:
        return jsonify({"error": "ModelExtractor not initialized."}), 500

    if not resume_text:
        return jsonify({"error": "Missing resume text"}), 400
    
    result = service_extractor.extract(resume_text)
    print(result)
    parsed_result = process_data(resume_text)

    return jsonify({"message": "Text analyzed", "data" : result})

