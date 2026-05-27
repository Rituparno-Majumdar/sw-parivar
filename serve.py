#!/usr/bin/env python3
"""
स्व-परिवार · SW-PARIVAR — Local development server.
Author: Rituparno Majumdar

Usage:
  python3 serve.py

Opens the app in your default browser automatically.
Press Ctrl+C to stop.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import signal

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, format, *args):
        if self.path == '/favicon.ico':
            return
        sys.stdout.write(f"  ⇢ {format % args}\n")
        sys.stdout.flush()


def main():
    os.chdir(DIR)

    lines = [
        f"  📚 स्व-परिवार · SW-PARIVAR",
        f"  Indian Social Work Knowledge Base",
        f"  📁 {DIR}",
        f"  🌐 http://localhost:{PORT}",
        f"  🔒 Press Ctrl+C to stop",
    ]
    w = max(len(l) for l in lines) + 4
    def box(l=None):
        if l is None: return "  ┌" + "─" * w + "┐"
        return "  │ " + l + " " * (w - len(l) - 1) + "│"
    print()
    print(box())
    for l in lines:
        print(box(l))
    print("  └" + "─" * w + "┘")
    print()

    webbrowser.open(f"http://localhost:{PORT}")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Server stopped.\n")
            httpd.server_close()
            sys.exit(0)


if __name__ == "__main__":
    main()
