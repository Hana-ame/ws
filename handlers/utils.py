import json5

def loads(s: str):
  return json5.loads(s)
def dumps(o) -> str:
  return json5.dumps(o)

def print_params(*args, **kwargs):
  print("Positional arguments:")
  for arg in args:
      print(arg)
  
  print("\nKeyword arguments:")
  for key, value in kwargs.items():
      print(f"{key}: {value}")

def test_print_params():
  # JSON5 string to be decoded
  json5_str = '''1
  '''

  # Decoding JSON5 string
  decoded_data = json5.loads(json5_str)

  print_params(**decoded_data)

if __name__ == '__main__':
  test_print_params()