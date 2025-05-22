from llama_cpp import Llama
import re


def extract_json_string_from_response(response: str) -> str | None:
    # Match the first valid-looking JSON block
    match = re.search(r'\{(?:[^{}]|(?R))*\}', response, re.DOTALL)

    if match:
        return match.group(0).strip()
    else:
        return None


class ModelExtractor:
  def __init__(self, model_path:str, max_ctx = 2048, threads = 8, gpu_layers = 0):
     self.llm = Llama(
                model_path=model_path,
                n_ctx=max_ctx,
                n_threads=threads,
                n_gpu_layers=0
                )
     
  def extract(self, resume:str)->str:
    prompt_resume = f"<resume>{resume}</resume>"
    prompt = prompt_resume + """
            <format>
            {
            "Basic Information": {
            "Name": "",
            "Contact": {
            "Email": "",
            "Phone": "",
            "Location": ""
            }
            },
            "Work Experience": {
            "Jobs": [
            {
            "Company": "",
            "Position": "",
            "Dates": "",
            "Responsibilities": [
            "",
            . . .
            ]
            },
            . . .
            ]
            },
            Skills": ["", . . . ],
            "Spoken Languages": ["", . . . ],
            "Summary" :  " .. your summary here"
            }
            </format>
            <task>
            extract resume data using this specified format, if some info is not found just put 'NA', identify skills yourself base on the whole resume not just the skill section and separate each skill  and also create a one sentences summary of the applicant:
            </task>
            """
    messages = [
      {
        "role": "user",
        "content": prompt
      }
    ]

    output = self.llm.create_chat_completion(
            messages=messages,
            stream=False,               # use True if you want real-time streaming
            max_tokens=32768,             # cap output size!
            temperature=0.1,
            repeat_penalty=1.1,         # Optional, helps reduce repetition
        )

    return extract_json_string_from_response(output['choices'][0]['message']['content'])