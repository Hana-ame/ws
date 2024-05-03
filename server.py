import asyncio
from websockets.server import serve
import handlers

def default_handler(data):
  return "no such hander."


async def echo(websocket, path):
  async for message in websocket:
    print(f"Received message: {message} @ {path}")

    result = (handlers.get(path) or default_handler)(message) or "from server.py: no result."

    print(f"Response result: {result}, @ {path}")
    await websocket.send(result)

async def main():
  async with serve(echo, "127.24.5.3", 8765):
    await asyncio.Future()  # run forever

asyncio.run(main())