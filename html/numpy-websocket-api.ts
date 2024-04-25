class WebSocketClient {
  private ws: WebSocket;

  constructor(url: string) {
    this.ws = new WebSocket(url);
    this.ws.onopen = () => {
      console.log(`WebSocket connection established to ${url}`);
    };
  }

  onmessage(callback: (data: string) => void) {
    this.ws.onmessage = (event) => {
      callback(event.data);
    };
  }

  send(data: string) {
    this.ws.send(data);
  }
}

class NumpyWebSocketClient extends WebSocketClient {
  
  constructor(url: string) {
    super(url);
  }

  onmessage(callback: (obj: any) => void) {
    super.onmessage((data: string) => {      
      callback(JSON.parse(data));
    });
  }

  send(data: any) {    
    super.send(JSON.stringify(data));
  }
}

// export default WebSocketClient;