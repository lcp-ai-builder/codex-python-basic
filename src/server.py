"""Simple HTTP server listening on port 5463.

中文说明：使用标准库 http.server 创建一个示例 HTTP 服务，方便本地调试。
"""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 5463


class SimpleHandler(BaseHTTPRequestHandler):
    """Minimal request handler returning a JSON message."""

    # 中文提示：仅示范 GET 请求，可按需扩展 POST/PUT 等方法。
    def do_GET(self) -> None:  # noqa: N802 (BaseHTTPRequestHandler 命名要求)
        """Handle GET request by returning JSON payload."""

        # 中文提示：设置 200 状态码并添加常见响应头。
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        # 中文提示：输出简单的 JSON 字符串作为响应体。
        self.wfile.write(b'{"message": "Hello from Codex server!"}')

    def log_message(self, format: str, *args: str) -> None:
        """Override noisy default logging to keep console clean."""

        # 中文提示：这里保留详细日志，便于初学者观察请求信息。
        super().log_message(format, *args)


def run_server() -> None:
    """Start the HTTP server."""

    # 中文提示：HTTPServer 需要 (host, port) 元组以及 handler 类。
    server = HTTPServer((HOST, PORT), SimpleHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    # 中文提示：serve_forever 会阻塞当前线程，直到 Ctrl+C 中断。
    server.serve_forever()


if __name__ == "__main__":
    run_server()
