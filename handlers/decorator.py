import traceback
import json5

def AutoJson(func):
  @AutoTryCatch
  def wrapper(s: str) -> str:
    kwargs = json5.loads(s)

    result = func(**kwargs)

    return str(json5.dumps(result))
  return wrapper

def AutoTryCatch(func):
  def wrapper(s: str) -> str:
    try:
      func(s)
    except Exception:      
      error_message = traceback.format_exc()
      return str(error_message)
  return wrapper