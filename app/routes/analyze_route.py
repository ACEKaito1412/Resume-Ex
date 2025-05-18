from flask import Blueprint, request, jsonify
from app.services.file_service import process_data


analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('analyze', methods=['POST'])
def analyze():
    """
    input_type:  application/json \n
    text: str 
    """
    data = request.get_json()   
    resume_text = data.get("text")

    if not resume_text:
        return jsonify({"error": "Missing resume text"}), 400
    
    parsed_result = process_data(resume_text)

    return jsonify({"message": "Text analyzed", "data" : parsed_result})

