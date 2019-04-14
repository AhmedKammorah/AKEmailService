# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-14 22:19:20
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-14 23:11:39
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
import socket
from threading import Thread
import requests

MOCK_SERVER_PORT = 10001

class AKMockHTTPRequestHandler(BaseHTTPRequestHandler):
    SPARKPOST_SEND_PATTERN = re.compile(r'/')
    def do_GET(self):
        if re.search(SPARKPOST_SEND_PATTERN, self.path):
            self.send_response(requests.codes.ok)
            # Add response headers.
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            # Add response content.
            response_content = json.dumps([])
            self.wfile.write(response_content.encode('utf-8'))
            return


def start_mock_server(server_port):
    server_base = 'localhost'
    mock_server = HTTPServer((server_base, server_port), AKMockHTTPRequestHandler)
    ser_thread = Thread(target=mock_server.serve_forever)
    ser_thread.setDaemon(True)
    ser_thread.start()