from llama_cpp import Llama
import re, os, json
from typing import Optional


def extract_json_string_from_response(response: str) -> Optional[dict]:
    try:
      # Match the first valid-looking JSON block
      match = re.search(r'```json(.*?)```', response, re.DOTALL)
      if match:
          json_str = match.group(1).strip()
      else:
          match = re.search(r'(\{.*\})', response, re.DOTALL)
          if match:
              json_str = match.group(1).strip()
          else:
              return None

      return json.loads(json_str)
    except json.JSONDecodeError:
       return None

def read_file(path: str) -> str:
   with open(path, mode='r', encoding='utf-8') as file:
      return file.read().strip() 


result_str = read_file(os.path.join(os.path.dirname(__file__), "../prompts", "result.txt"))

class ModelExtractor:
  def __init__(self, model_path:str, max_ctx = 2048, threads = 8, gpu_layers = 0):
     self.llm = Llama(
                model_path=model_path,
                n_ctx=max_ctx,
                n_threads=threads,
                n_gpu_layers=0
                )
    
     # load_promt
     base_path = os.path.join(os.path.dirname(__file__), "../prompts")
     self.format_text = read_file(os.path.join(base_path, "format.txt"))
     self.task_text = read_file(os.path.join(base_path, "task.txt"))


  def test_res(self):
    return extract_json_string_from_response(result_str)

  def extract(self, resume:str)->str:
    prompt = (
       f"<resume>{resume}</resume>"
       f"<format>{self.format_text}</format>"
       f"<task>{self.task_text}</task>"
    )

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
            temperature=0.01,
            repeat_penalty=1.1,         # Optional, helps reduce repetition
        )

    return extract_json_string_from_response(output['choices'][0]['message']['content'])