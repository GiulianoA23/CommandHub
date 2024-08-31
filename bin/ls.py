# ls.py: Lists directories and files in the current working directory.

import os

def run(command):
    print("Contents of directory:", os.getcwd())
    for item in os.listdir():
        print(item)
