import PyPDF2, spacy, openai, ast, random
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

# Load Spacy NLP Trained Model
nlp = spacy.load("./model-best")

# Load OpenAi Key
API_KEY = "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"
openai.api_key = API_KEY

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///resource.db")


# 
@app.route("/")
def index():
    return render_template('index.html', navigation = True)


# This route will handle the page for uploading resume
@app.route("/upload_resume", methods=["GET", "POST"])
def upload_resume():

    # This will check if the request method is POST from the UI
    if request.method == "POST":
        method = request.form.get('method')
        
        if "resume" not in request.files:
            flash("No File Part")
            return redirect(request.url)

        resume_file = request.files["resume"]

        if resume_file.filename == "":
            flash("No File Selected")
            return redirect(request.url)

        allowed_ext = {
            "pdf"
        }

        # Will Check if the file uploaded is a pdf 
        if resume_file.filename.split(".")[-1].lower() not in allowed_ext:
            flash("Invalid File Format: Only Pdf's are Allowed")
            return redirect(request.url)

        pdf_data = None
        try:
            # Read the pdf and extract the information/text
            pdf_reader = PyPDF2.PdfReader(resume_file)
            num_pages = len(pdf_reader.pages)

            pdf_data = ""

            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                pdf_data = page.extract_text()

            # Extract the Information base on method
            data = extractData(pdf_data, method)
            
            # Save the data to out database
            try:
                # Add to history
                db.execute("INSERT INTO data (type, resume, annotation) VALUES (?,?,?)",
                        int(method), pdf_data, str(data))
            except Exception as e:
                print(e)

        except Exception as e:
            flash("Error while Reading File")
            return redirect(request.url)

        return render_template("upload.html", navigation = False, data = data, method = method)

    method = request.args.get('method')
    return render_template("upload.html", method = method, navigation = False)


# This route will show the data of uploaded file on the server
@app.route("/data")
def data():
    rows = db.execute("SELECT * FROM data")
    return render_template("data.html", navigation = False, data = rows)

# Functions 
# This function will check what type of method is on and give it to 
# corresponding function
def extractData(text, type):
    if type == "0":
        data = spacyMode(text)
        return data
    else:
        data = gptMode(text)
        return data

# This function will extract information using the best-model on our Trained
# NER and return the extracted info
def spacyMode(resume):
    doc = nlp(resume)
    data = []
    for ents in doc.ents:
        # Write the results to the variable
        data.append([ents.text, ents.label_])

    return data

# This gptMode will use the resume and the promt to load and extract the data that we wanted
def gptMode(resume):
    promt = """id like for you to search for this labels here and only needed the exact text and its label, no need to put the labels annotation if null, do not put text when no  label is found, output it on json format on one list ,make sure information and its label is in this format ['Text',  'label'], separate each skill, verify if the label found for text is correct, remove null and duplicates:
    ['Personal Information: Full Name', 'Personal Information: Phone Number', 'Personal Information: Email Address', 'Personal Information: Address', 'Work Experience: Company/Organization Name',
    'Work Experience: Job Title', 'Work Experience: Dates of Employment', 'Education: Degree/Certification Name', 'Education: Institution Name', 'Education: Location',
    'Education: Dates of Attendance/Graduation','Skills: Technical Skills','Skills: Soft Skills']"""

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system", "content": "You are an expert applicant handler: " + promt},
            {"role":"user", "content": resume}
        ]
    )

    # Extract the message content from the json response
    message_content = response['choices'][0]['message']['content']

    # Save the data as list
    data = ast.literal_eval(message_content)
    
    return data