import os
import time

def create_crud_log(lang: str, title: str, crud_type: str):
    filename = "crud_log.csv"
    file_exists = os.path.isfile(filename)

    if not file_exists:
        with open(filename, "w") as f:
            f.write("Lang, Title, Type, Date")
    else:
        date = time.strftime("%b %d %Y", time.localtime())
        with open(filename, "a") as f:
            f.write(f"\n{lang},{title},{crud_type},{date}")