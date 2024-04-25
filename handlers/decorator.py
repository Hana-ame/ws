import traceback
import json5

def AutoJson(func):
  def wrapper(s: str) -> str:
    try:
      kwargs = json5.loads(s)

      result = func(**kwargs)

      return str(json5.dumps(result))
    except Exception:
      error_message = traceback.format_exc()
      return str(error_message)
    finally:
      # print("what")
      pass
  return wrapper
