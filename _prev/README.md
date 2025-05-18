# RESUME-EXTRACTOR

![Project Title](./static/logo-dark.png)

## Description

Welcome to My Project Resume-Ex, Resume-Ex is for people who's tired of manually extracting resume data from pdf. Through the use of GPT model or a Pre-trained NER using Spacy we could extract critical information from the file that the user uploaded. We could also use the data that was extracted by using the GPT API to train new NER. 

The repository includes separate directories where u can train new model and run the web-application.

- `Training`: Contains the code and instructions on how you can train your own NER.
  
- `Web-Application`: Contains the code and instructions for the web-application.

## Video Links

#### [`CS50 Project: Resume-Ex Presentation`](https://youtu.be/VEZghCH6xw0)
#### [`CS50 Project: Resume-Ex Web-View`](https://youtu.be/cUWfLBwUkP0)

## Table of Contents
- [RESUME-EXTRACTOR](#resume-extractor)
  - [Description](#description)
  - [Video Links](#video-links)
      - [`CS50 Project: Resume-Ex Presentation`](#cs50-project-resume-ex-presentation)
      - [`CS50 Project: Resume-Ex Web-View`](#cs50-project-resume-ex-web-view)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
  - [Reference](#reference)

## Features

This project offers two feature for extracting information from resume that is uploaded:

1. **Spacy-Based NER:**
   - With our Spacy-based NER feature, we've trained a specialized model to recognize and extract specific entities from resumes. These entities include critical details such as names, skills, and other pertinent information. While our NER model is still being refined, it offers impressive accuracy. 

2. **OpenAI API Integration:**
   - For those seeking advanced language comprehension and contextually relevant data retrieval, our GPT-3 API integration is the ideal solution. By leveraging OpenAI's GPT-3, we've unlocked the power of deep learning to enhance your experience. The GPT-3 model understands the context of the extracted data, resulting in even more precise and meaningful information retrieval.


## Getting Started

### Installation

1. Get this link and clone repository : git clone `https://github.com/ACEKaito1412/Resume-Ex.git`
2. Create new environment using pyenv make sure to install python version 3.10.11
3. Activate the environment
4. Install requirement.txt

### Usage
1. Start the application: flask run
2. Click the link or go to `http://localhost:5000`
3. Navigate to the features on the web application and upload a file.
4. You can check the uploaded result on `/data`

## Technologies Used
- Python Version 3.10.11
- Flask Version 2.3.2
- PyPDF2 Version 3.0.1
- Spacy Version 3.6.0
- OpenAI API Version 0.27.8


## Contributing

We welcome contributions to enhance Resume-Ex. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push the branch to your fork: `git push origin feature-name`.
5. Submit a pull request to the main repository.

## License

The software is released under the UnLicense.

UNLICENSE

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

## Contact

For any questions or inquiries about the Resume-Ex project, please contact [Jhun Carlo Macdon](mailto:macdon.jc.bscs@gmail.com).

## Reference

Here are my reference for this project please check the blog bellow if you wanted to create your custom NER:

- [`Build Resume Parser using Spacy Version 3`](https://www.youtube.com/watch?v=C23DAW5iSiA)
- [`Blog On Resume Parser`](https://www.romanshilpakar.com.np/blog/6)
- [`OpenAI API Reference on Completion`](https://platform.openai.com/docs/api-reference/completions)
