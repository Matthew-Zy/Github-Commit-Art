from datetime import datetime, timedelta

from typing import List
import random
import subprocess
import sys, os
from pathlib import Path

file_name: str = "hey/amongla.txt"
path = Path(file_name)


Random_commit_msg: List[str] = [
    "Pikachu", "Obama", "Sussy AMogus"
]
Random_content_msg: List[str] = [
    "wow", "I love", "The mona"
]


today = datetime.today()
print(today.day)
print(today)

print(timedelta(days=today.weekday()))

def make_commit(days_ago: int):
    date = datetime.today()
    dateStr = date.strftime("%a %b %d %I:%M %Y")
    print(dateStr)
    with open(file_name, "a") as f:
        f.write("soy")
    # subprocess.run(["git", "add", file_name])
    # subprocess.run(["git", "commit", file_name, f'{days_ago} day ago', "-m", "random"]) # both should theoretically work
    # subprocess.run(["git", "commit", "--amend", "-m", "some stuff", f'--date="{dateStr}"',])

make_commit(0)