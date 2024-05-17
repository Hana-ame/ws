import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("API_KEY"))
system_prompt = os.getenv("SYSTEM_PROMPT")
print(system_prompt)


def api(prompt:str="", content: str="") -> str:
  if prompt == "":
    prompt = system_prompt
  completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
      {
        "role": "system",
        "content": prompt,
      },
      {"role": "user", "content": content},
    ],
    temperature=1,
    max_tokens=None,
    top_p=1,
    stream=False,
    stop=None,
  )

  return completion.choices[0].message.content, True

if __name__ == "__main__":
  print(api('bangdream 是什么'))
  print(api('为什么要演奏春日影'))
  print(api('我是谁'))
  print(api('你是谁'))