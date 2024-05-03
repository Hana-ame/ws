import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("API_KEY"))

def api(data: str) -> str:
  content = data
  completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
      {
        "role": "system",
        "content": "你能说中文吗，如果可以请用中文回答我下面的问题。回答前明确将要回答的内容，回答时请尽可能地详细。",
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
