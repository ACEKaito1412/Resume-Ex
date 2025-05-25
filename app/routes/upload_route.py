from flask import Flask, Blueprint, request, jsonify, render_template
from app.services.file_service import ALLOWED_FILES, save_document, allowed_file
from app.services.file_service import get_text_from_docx, get_text_from_pdf
from app.services.resume_extractor import ModelExtractor

service_extractor = None

upload_bp = Blueprint('upload', __name__)

def init_upload_route(extractor:ModelExtractor):
    global service_extractor
    service_extractor = extractor

@upload_bp.route('/upload', methods=["POST", "GET"])
def upload():
    """
    input_type: multipart/form-data \n
    file: docx/pdf \n
    file_type: docx/pdf
    """

    if not service_extractor:
        return jsonify({"message" : "Model extractor not defined"}), 400

    if request.method == "POST":
        if 'file' not in request.files:
            return jsonify({"message" : "No file part"}), 400

        file = request.files['file']
        file_type = request.form.get('file_type')
        
        if not allowed_file(filename=file.filename):
            return jsonify({"message" : "File type not allowed"}), 400
        
        if file_type not in ALLOWED_FILES:
            return jsonify({
                "message" : "File type not allowed"
            })

        path, error = save_document(file=file)
        

        if file_type == 'docx':
            resume_text = get_text_from_docx(path)
        elif file_type == 'pdf':
            resume_text = get_text_from_pdf(path)

        print(resume_text)
        extracted_result = service_extractor.extract(resume=resume_text)

        if error:
            return jsonify({"message" : error})
        
        return jsonify({"message" : "resume analyzed", "data" : extracted_result}), 200
    
    return render_template('upload.html')