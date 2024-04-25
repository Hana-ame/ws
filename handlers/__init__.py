from typing import Callable
from .decorator import AutoJson

handlers:dict[str, Callable[[str], str]] = {}

def get(path: str) -> Callable[[str], str]:
  return handlers.get(path)

# unused.
def add_handler(path: str, handler: Callable[[str], str]):
  handlers[path] = handler

from .echo import echo
handlers["/echo"] = echo

from .np import a_lmul, a_transpose
handlers["/a/lmul"] = AutoJson(a_lmul)
handlers["/a/transpose"] = AutoJson(a_transpose)