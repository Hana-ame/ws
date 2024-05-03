import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("API_KEY"))

def api(data: str) -> str:
  content = data
  completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
      {
        "role": "system",
        "content": "请用中文回答我下面的问题。回答前明确将要回答的内容，回答时请尽可能地详细。如果回答的是英文，请将英文翻译成中文。请一定要用中文回答。",
      },
      {"role": "user", "content": content},
    ],
    temperature=1,
    max_tokens=None,
    top_p=1,
    stream=False,
    stop=None,
  )

  return completion.choices[0].message.content

if __name__ == "__main__":
  print(api('为啥不行'))