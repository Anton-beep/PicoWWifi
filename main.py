# Only runs src/main.py
import os

os.chdir("src")

try:
    exec(open("main.py").read())
except Exception as ex:
    print(ex)

os.chdir("..")
