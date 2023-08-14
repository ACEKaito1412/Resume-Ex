import openai, json

# Save Key
API_KEY = "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"
openai.api_key = API_KEY

# Ready Customize Prompt
text = """id like for you to search for this labels here and only needed the exact text and its label, no need to put the labels annotation if null, do not put text when no  label is found, output it on json format on one list ,make sure information and its label is in this format ['Text',  'label'], separate each skill, verify if the label found for text is correct, remove null and duplicates:
['Personal Information: Full Name', 'Personal Information: Phone Number', 'Personal Information: Email Address', 'Personal Information: Address', 'Work Experience: Company/Organization Name',
 'Work Experience: Job Title', 'Work Experience: Dates of Employment', 'Education: Degree/Certification Name', 'Education: Institution Name', 'Education: Location',
 'Education: Dates of Attendance/Graduation','Skills: Technical Skills','Skills: Soft Skills']"""

resume = """Kristine Kihn 12B, Violet Apartments Kingston Avenue, Phoenix, AZ 85006 123 345 7890 Email: Porfirio.Hauck@baab.io Career Objective: Secure the position of a digital advertising executive and use my competence in advertising and marketing for helping the organization in meeting their goals and building a strong reputation in the market. Key Skills: Competent in planning strategies and developing objectives Knowledge of content development standards and digital advertising norms Thorough understanding of the applications of PHP , JavaScript , XHTML , Adobe , etc. Skilled at initiating innovative brand development ideas and promotion strategies Efficient at identifying the nature, reactions and preferences of the customers Hold up to date information on Search Engine Marketing SEM , Search Engine Optimization SEO , Sponsored Search, Email Advertising, and Social Media Marketing Educational Qualification: Bachelor's Degree in Advertising and Marketing Management Phoenix University , 2008 Work Experience: Designation: Digital Advertising Executive Organization: Violet Advertisers , Phoenix, AZ Duration: May 2010 till date Devise advertising and marketing strategies as per the product nature and target audience Issue topic names and product details to copywriters for writing promotional content Inspect the organization's website and give an overview of its designs and functionality Suggest ideas to promote the services of e commerce and online shopping Establish friendly interaction with customers and receive their feedback Communicate with market analysts to study the demographics and identify the target audience Designation: Digital Advertising Assistant Organization: Mayfair Advertisers , Phoenix, AZ Duration: January 2009 April 2010 Prepared the different audio and visual materials to promote the organization's goods Provided the product's pictures and list of features on the Internet for customer's reference Coordinated with the team of SEOs, writers and designers to generate eye catching promotional content Drafted reports of the stocks that are most viewed and liked by the customers and that sold in higher quantities Created interesting promotional content and included animations, audios and articles to spark readers' interest Designation: Information Developer Organization: Matrix Advertisers , Phoenix, AZ Duration: December 2007 December 2008 Developed promotional articles enriched with products' key features based on the understanding derived from consultation with clients Coordinated with the graphic designers and animators to make interesting and interactive presentations Updated information on the website as per the new products or versions that are introduced by the organization Provided answers to customer queries and forwarded their purchase orders Extracurricular Activities: Participated and organized fund raising events for children under 16 in order to help them choose desired careers. This activity helped me in developing leadership skills and understanding the importance of teamwork Contributed my efforts in spreading awareness of global warming through blogs and publishing my articles in local newspapers Active member of City Bikers' Club for seven years Reference Kristine Kihn Chief Advertising Manager Violet Advertisers , Phoenix, AZ 688 754 1489 Email: Porfirio.Hauck@baab.io"""

response_json = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role":"system", "content": "You are an expert applicant handler: " + text},
        {"role":"user", "content": resume}
    ]
)

response_data = json.loads(response_json)

# Write the message content to Output File
with open('output.txt', 'w') as file:
    file.write(response_data['choices'][0]['message']['content'])
