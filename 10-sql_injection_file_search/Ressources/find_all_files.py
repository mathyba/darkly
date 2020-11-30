#!/usr/bin/python3

"""Search all images"""

import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data.startswith(("ID", "Title", "Url")):
            print(data)

parser = MyHTMLParser()

for i in range(1, 100):
    r = requests.get(f"http://192.168.0.160/?page=searchimg&id={i}&Submit=Submit#")
    parser.feed(r.text)

