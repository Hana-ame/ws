var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var WebSocketClient = /** @class */ (function () {
    function WebSocketClient(url) {
        this.ws = new WebSocket(url);
        this.ws.onopen = function () {
            console.log("WebSocket connection established to ".concat(url));
        };
    }
    WebSocketClient.prototype.onmessage = function (callback) {
        this.ws.onmessage = function (event) {
            callback(event.data);
        };
    };
    WebSocketClient.prototype.send = function (data) {
        this.ws.send(data);
    };
    return WebSocketClient;
}());
var NumpyWebSocketClient = /** @class */ (function (_super) {
    __extends(NumpyWebSocketClient, _super);
    function NumpyWebSocketClient(url) {
        return _super.call(this, url) || this;
    }
    NumpyWebSocketClient.prototype.onmessage = function (callback) {
        _super.prototype.onmessage.call(this, function (data) {
            callback(JSON.parse(data));
        });
    };
    NumpyWebSocketClient.prototype.send = function (data) {
        _super.prototype.send.call(this, JSON.stringify(data));
    };
    return NumpyWebSocketClient;
}(WebSocketClient));
// export default WebSocketClient;
