#!/usr/bin/env python3
"""
aai_token_server.py — TANNY's AssemblyAI temp-token minter.

Runs alongside server.py (your Groq daemon). Same philosophy: the real
API key never touches the browser. TANNY's frontend calls this server,
gets a short-lived temp token, and uses THAT to open the AssemblyAI
streaming WebSocket directly.

Setup:
    setx ASSEMBLYAI_API_KEY "your-key-here"      (Windows, then reopen terminal)
    export ASSEMBLYAI_API_KEY="your-key-here"     (macOS/Linux)

Run:
    python aai_token_server.py
    -> listens on http://127.0.0.1:8766/token

No external dependencies — stdlib only, so there's nothing to pip install.
"""

import json
import os
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8766
API_KEY = os.environ.get("ASSEMBLYAI_API_KEY", "").strip()
TOKEN_URL = "https://streaming.assemblyai.com/v3/token?expires_in_seconds=60"


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path.rstrip("/") != "/token":
            self.send_response(404)
            self._cors()
            self.end_headers()
            self.wfile.write(b'{"error":"not found"}')
            return

        if not API_KEY:
            self.send_response(500)
            self._cors()
            self.end_headers()
            self.wfile.write(
                b'{"error":"ASSEMBLYAI_API_KEY not set on this machine"}'
            )
            return

        try:
            req = urllib.request.Request(
                TOKEN_URL, headers={"Authorization": API_KEY}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                body = resp.read()
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        except Exception as e:
            self.send_response(502)
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, fmt, *args):
        pass  # keep the console quiet


if __name__ == "__main__":
    if not API_KEY:
        print("⚠  ASSEMBLYAI_API_KEY is not set — /token will return 500 until it is.")
    print(f"TANNY AssemblyAI token server → http://127.0.0.1:{PORT}/token")
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
