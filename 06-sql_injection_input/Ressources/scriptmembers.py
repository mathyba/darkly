#!/usr/bin/python3

"""Script to check all members"""

import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    """Parse output"""

    def handle_data(self, data):
        """Ignore irrelevant and print relevant output"""
        ignore = [
        "© BornToSec", "BornToSec - Web Section", "Home", "Survey", "Members", "Search member by ID:"
        ]

        data = data.strip()

        if not len([line for line in ignore if line in data]) and len(data):
            print(data)

parser = MyHTMLParser()

if __name__=="__main__":
    for id in range(1, 11):
        r = requests.get(f"http://192.168.0.160/?page=member&id={id}&Submit=Submit#")
        parser.feed(r.text)
