import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("API_KEY"))
system_prompt = os.getenv("SYSTEM_PROMPT")
print(system_prompt)


def api(data: str) -> str:
  content = data
  completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
      {
        "role": "system",
        "content": system_prompt,
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