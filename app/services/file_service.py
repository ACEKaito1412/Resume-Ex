import os
from werkzeug.utils import secure_filename
import uuid
import fitz
from docx import Document
from typing import Dict, Any

ALLOWED_FILES = ['pdf', 'docx']
UPLOAD_FOLDER = "app/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename:str):
    print(filename.split('.', 1)[1].lower())
    print(filename.split('.', 1)[1].lower() in ALLOWED_FILES)

    return filename.split('.', 1)[1].lower() in ALLOWED_FILES


def save_document(file) -> list[str, str]:
    try:
        filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        return file_path, ""
    except Exception as e:
        return "", str(e)
    
def get_text_from_pdf(file_path)->str:
    doc = fitz.open(file_path)

    text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        text += page.get_text()

    doc.close()

    return text

def get_text_from_docx(file_path)->str:
    text = []
    with open(file_path, 'rb') as f:
        doc = Document(f)

        for parag in doc.paragraphs:
            if parag.text.strip():
                text.append(parag.text.strip())

    return '\n'.join(text)


def process_data(text_data:str)->Dict[str, Any]:
    extracted_data = {
        'name' : 'juan delacrux',
        'email' : 'delacrux@samail.com',
        "skills": ["Python", "Flask", "NLP"]
    }

    return extracted_data