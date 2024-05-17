import traceback
import json5

def AutoJson(func):
  @AutoTryCatch
  def wrapper(s: str) -> str:
    kwargs = json5.loads(s)

    result, direct = func(**kwargs)
    
    if direct:
      return result
    return str(json5.dumps(result))
  return wrapper

def AutoTryCatch(func):
  def wrapper(s: str) -> str:
    try:
      return func(s)
    except Exception:
      print(traceback.format_stack())
      error_message = traceback.format_exc()
      return str(error_message)
  return wrapper