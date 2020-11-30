#!/usr/bin/python3

"""Parse all READMEs in a directory tree"""

import os
from html.parser import HTMLParser

import requests

dirpath = os.getenv("PWD", "/home/darkly")
links = []


def find_all_readmes(path="http://192.168.0.160/", targets=[".hidden/"]):
    """
    Recursively checks

    Args:

        path: dirpath of the URL of the request

        targets: list of targets in the path directory
    """

    for item in targets:
        parser = MyHTMLParser(path + item)
        resp = requests.get("%s%s" % (path, item))
        print("look into %s%s" % (path, item))
        parser.feed(resp.text)
        for readme in parser.readmes:
            resp = requests.get(readme)
            if not any(
                [
                    l
                    for l in [
                        "Moi aussi !",
                        "de gauche",
                        "de droite",
                        "craquer non ?",
                        "du dessous",
                        "du dessus",
                        "pas bon",
                    ]
                    if l in resp.text
                ]
            ):
                with open(f"{dirpath}/outputhidden.txt", "a+") as myfile:
                    myfile.write(resp.text)

        find_all_readmes(path + item, parser.links)


class MyHTMLParser(HTMLParser):
    """HTML Parser"""

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.links = []
        self.readmes = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    if value.startswith("README"):
                        self.readmes.append(self.path + value)
                    elif not value.startswith(("..")):
                        self.links.append(value)


find_all_readmes()
